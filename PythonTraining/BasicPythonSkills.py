'''
Author: Fionn Mcguire
Lynda.com python training
'''


print("Hello World")
a,b = "Fionn","Python 3"


#Note that when using format, if you're printing the variables in order, you can use
#{}, if you want to reuse the variables and/or print them out of order you can use {0} or {1}

print("Hello {0}, you're programming in {1}".format(a,b))
print("{1} is the language you're programming in {0}, isn't {1} good?".format(a,b))

x,y = 6,7

if x < y:
    print("{} is less than {}".format(x,y))
else:
    print("{} is less than {}".format(y,x))

#You can also place a simple if inside the print statement
print("Nice" if x < y else "One")

#Demonstrating a while loop fibonacci series 
a,b,c = 1,1,5000
while a < c:
    print(a)
    d = a+b
    b = a
    a = d

#Demonstrting for loop
for x in range (0 , 10):
    print("Index {}".format(x))

def isPrime(x):
    if x == 0 or x == 1:
        print("{} is Prime (Debatable)".format(x))
    else:
        i = 2
        checker = True
        while i < x:
            if x%i == 0:
                checker = False
                exit
            i+=1
        if checker == True:
            print("{} is Prime".format(x))
        
i = 0
while i < 100:
    isPrime(i)
    i+=1
    

    
