# Configure the AWS Provider
provider "aws" {
  region = "us-east-1"
  access_key = "AKIAQH5RXYCP4CT6M2VF"
  secret_key =  "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"
}


#Terraform Variables
variable "subnet_prefix"{
    description = "Repr CIDR block for the subnet"
    type = string
}

#1. Create VPC 

resource "aws_vpc" "prod-terraform-vpc" {
    cidr_block = "10.0.0.0/16"
    tags = {
        Name = "Production"  
    }
}

#2. Create internet gateway 

resource "aws_internet_gateway" "gw" {
  vpc_id = aws_vpc.prod-terraform-vpc.id

  tags = {
    Name = "main"
  }
}

#3. Create Custom Route Table 

resource "aws_route_table" "prod-route-table" {
  vpc_id = aws_vpc.prod-terraform-vpc.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.gw.id
  }  

  route {
    ipv6_cidr_block        = "::/0"
    gateway_id = aws_internet_gateway.gw.id
  }

  tags = {
    Name = "Prod-Route-Table"
  }
}

#4. Create a subnet 

resource "aws_subnet" "subnet-1" {
  vpc_id     = aws_vpc.prod-terraform-vpc.id
  cidr_block = var.subnet_prefix
  availability_zone = "us-east-1a"

  tags = {
    Name = "prod-subnet"
  }
}

#5. Associate Subnet with Route Table 

resource "aws_route_table_association" "a" {
    subnet_id = aws_subnet.subnet-1.id
    route_table_id = aws_route_table.prod-route-table.id
}
#6. Create a security group to allow traffic to port 22,443,80

resource "aws_security_group" "allow_web" {
  name        = "allow_web_traffic"
  description = "Allow Web inbound traffic"
  vpc_id      = aws_vpc.prod-terraform-vpc.id

  ingress {
    description = "HTTPS Traffic"
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

 ingress {
    description = "HTTPS Traffic"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

 ingress {
    description = "HTTPS Traffic"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "allow_web"
  }
}

#7. Create a network interface with an IP in the subnet that was created in step 4

resource "aws_network_interface" "web_server_nic" {
  subnet_id       = aws_subnet.subnet-1.id
  private_ips     = ["10.0.1.50"]
  security_groups = [aws_security_group.allow_web.id]
}

#8. Create an elastic IP to the network interface created in step 7

resource "aws_eip" "lb" {
  vpc      = true
  network_interface = aws_network_interface.web_server_nic.id
  associate_with_private_ip = "10.0.1.50"
  depends_on = [aws_internet_gateway.gw]
}

# Prints the public IP in the console once the terraform apply command is executed
output "server_public_ip" {
    value = aws_eip.lb.public_ip
}
#9. Create ubuntu server and install/enable apache2

resource "aws_instance" "web" {
    ami = "ami-042e8287309f5df03"
    instance_type = "t2.micro"
    availability_zone = "us-east-1a"
    key_name = "terraform-key"

    network_interface {
        device_index = 0
        network_interface_id = aws_network_interface.web_server_nic.id
    }
    

    user_data = <<-EOF
                #! /bin/bash
                sudo apt update -y
                sudo apt install apache2 -y
                sudo systemctl start apache2
                sudo bash -c 'echo My First Terraform Web Server > /var/www/html/index.html'
                EOF
    
    tags = {
        Name = "Prod Web Server"
    }
}
