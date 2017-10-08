'''
Author: Fionn Mcguire
Date: 08-10-2017
Description: Linked lists practice, speed and manipulation

'''
class Node(object):
    def __init__(self,d,n = None):
        self.data = d
        self.next = n
    def getnext(self):
        return self.next
    def getdata(self):
        return self.data
    def setnext(self,n):
        self.next = n
    def setdata(self,d):
        self.data = d

class LinkedList(object):
    def __init__(self,r = None):
        self.root = r
        self.size = 0
    def getsize(self):
        return self.size
    def addnode(self,d):
        new_node = Node(d,self.root)
        self.root = new_node
        self.size+=1
    def removenode(self,d):
        this_node = self.root
        prev_node = None
        while this_node:
            if this_node.getdata() == d:
                if prev_node:
                    prev_node.setnext(this_node.getnext())
                else:
                    self.root = this_node.getnext()
                self.size-=1
                return True
            else:
                prev_node = this_node
                this_node = this_node.getnext()
        return False

list1 = LinkedList()
list1.addnode(5)
list1.addnode(11)
list1.addnode(17)
list1.addnode(6)
list1.addnode(8)
list1.addnode(3)
list1.addnode(34)
list1.addnode(1)
list1.removenode(17)
list1.removenode(34)

current_node = list1.root

while current_node:
    print(current_node.getdata())
    current_node = current_node.getnext()
