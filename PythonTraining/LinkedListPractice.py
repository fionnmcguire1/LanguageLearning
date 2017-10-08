'''
Author: Fionn Mcguire
Date: 08-10-2017
Description: Linked lists practice, speed and manipulation

'''

class Node(object):
    def __init__(self,d,n,p = None):
        self.data = d
        self.next = n
        self.prev = None
    def getnext(self):
        return self.next
    def setnext(self,n):
        self.next = n
    def setdata(self,d):
        self.data = d
    def getdata(self):
        return self.data
    def getprev(self):
        return self.prev
    def setprev(self,p):
        self.prev = p

class Linkedlist(object):
    def __init__(self, r = None):
        self.root = r
        self.size = 0
    def getsize(self):
        return self.size
    def add(self,d):
        new_node = Node(d,self.root)
        if self.getsize() > 1: 
            next_node = new_node.getnext()
            next_node.setprev(new_node)
        self.root = new_node
        self.size+=1
    def remove(self,d):
        prev_node = None
        this_node = self.root
        while this_node:
            if this_node.getdata() == d:
                if this_node.getprev():
                    prev_node = this_node.getprev()
                    prev_node.setnext = this_node.getnext()
                else:
                    self.root = this_node.getnext()
                self.size-=1
                return True
            else:
                this_node = this_node.getnext()
        return False
#Appending data to the list
list1 = Linkedlist()
list2 = Linkedlist()
list3 = Linkedlist()
for i in range(20):
    list1.add(i)
    list2.add(i**2)


#Adding 2 linked lists
current_node = list1.root
current_node2 = list2.root
while current_node:
    result = current_node.getdata()+current_node2.getdata()
    list3.add(result)
    current_node = current_node.getnext()
    current_node2 = current_node2.getnext()


#Printing the resulting list
current_node = list3.root
while current_node:
    print(current_node.getdata())
    current_node = current_node.getnext()




                
        



                
            
        
                

        
