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
    #print(current_node.getdata())
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
    #print(current_node.getdata())
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
        self.root = newnode
        if self.size > 0:
            newnode.next = currentnode
            tailnode = self.tail
            tailnode.next = self.root
            rootnode = self.root
            rootnode.prev = self.tail
        else:
            self.tail = newnode

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
    def rotate(self,n):
        for i in range(n):
            rootnode = self.root
            tailnode = self.tail
            #print("{} Root Node: {}".format(i,rootnode.data))
            #print("{} Tail Node: {}".format(i, tailnode.data))
            self.root = rootnode.next
            self.tail = tailnode.next

list2 = linkedlist()
for i in range(20):
    list2.add(i)
list2.rotate(5)

currentnode = list2.root
print("Root Node: {}".format(currentnode.data))

while currentnode != list2.tail:
    print(currentnode.data)
    currentnode = currentnode.next

tailnode = list2.tail
print("Tail Node: {}".format(tailnode.data))


'''Hackerank Medium Question, check if linked list data structure is cyclic'''
def has_cycle(head):
    aryOfPointers = []
    while head:
        if head.next:
            if head.next in aryOfPointers:
                return True
            else:
                aryOfPointers.append(head)
                head = head.next
        else:
            return False
    return False
