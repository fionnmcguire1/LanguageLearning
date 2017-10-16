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
        if self.getsize() > 0:
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


#Reverse a linked list
current_node = list3.root
counter = 0
while current_node:
    if counter == list3.getsize()-1:
        list3.root = current_node
    next_node = current_node.getnext()
    if current_node.getprev():
        prev_node = current_node.getprev()
        current_node.setprev(next_node)
        current_node.setnext(prev_node)
    else:
        current_node.setprev(current_node.getnext())
        current_node.setnext(None)
    current_node = current_node.getprev()
    counter+=1

current_node = list3.root
while current_node:
    print(current_node.getdata())
    current_node = current_node.getnext()


#Create a doubly linked list, keep track of head and tail
class node(object):
    def __init__(self,d,n=None,p=None):
        self.data = d
        self.next = n
        self.prev = p


class linkedlist(object):
    def __init__(self,r=None,t=None):
        self.root = r
        self.tail = t
        self.size = 0
    def add(self,d):
        newnode = node(d)
        if self.root is not None:
            currentnode = self.root
            currentnode.prev = newnode
        else:
            self.root = newnode
        if self.size > 0:
            newnode.next = currentnode
        else:
            self.tail = newnode
        self.root = newnode
        self.size+=1
    def remove(self,d):
        currentnode = self.root
        prevnode = None
        while currentnode:
            if currentnode.data == d:
                if prevnode:
                    prevnode.next = currentnode.next
                    nextnode = currentnode.next
                    nextnode.prev = prevnode
                else:
                    self.root = currentnode.next
                self.size -=1
            else:
                currentnode = currentnode.next
        return False

list2 = linkedlist()
list2.add(8)
list2.add(9)
list2.add(10)
list2.add(11)
list2.add(12)
list2.add(13)
list2.add(14)
list2.add(15)
list2.add(16)
list2.add(17)
list2.add(18)
list2.add(19)
list2.add(20)
list2.add(21)
list2.add(22)
list2.add(23)
list2.add(24)

currentnode = list2.root
while currentnode:
    print(currentnode.data)
    currentnode = currentnode.next

tailnode = list2.tail
print("Tail Node: {}".format(tailnode.data))
