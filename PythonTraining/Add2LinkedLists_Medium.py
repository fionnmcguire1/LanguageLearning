'''
Author: Fionn Mcguire
Date: 21-09-2017
Add 2 linked lists together
'''
            
            
class Node(object):
    def __init__(self,d,n = None):
        self.data = d
        self.next = n
    def getnext(self):
        return self.next
    def setnext(self,n):
        self.next = n
    def getdata(self):
        return self.data
    def setdata(self,d):
        self.data = d

class LinkedList (object):
    def __init__(self, r = None):
        self.root = r
        self.size = 0
    def getsize(self):
        return self.size
    def add_data(self,d):
        new_node = Node(d, self.root)
        self.root = new_node
        self.size +=1
    def remove(self,d):
        this_node = self.root
        prev_node = None
        while this_node:
            if this_node.getdata() == d:
                if prev_node:
                    prev_node.setdata(this_node.getnext())
                else:
                    self.root = this_node
                self.size -=1
                return True
            else:
                prev_node = this_node
                this_node = this_node.getnext()
        return False

list1 = LinkedList()
list1.add_data(5)
list1.add_data(11)
list1.add_data(17)
list1.add_data(6)
list1.add_data(8)
list1.add_data(3)
list1.add_data(34)
list1.add_data(1)

list2 = LinkedList()
list2.add_data(5)
list2.add_data(11)
list2.add_data(17)
list2.add_data(6)
list2.add_data(8)
list2.add_data(3)
list2.add_data(34)
list2.add_data(1)


def addTwoNumbers(list1, list2):
    list3 = LinkedList()
    this_node = list1.root
    this_node2 = list2.root
    i = 0
    while this_node:       
        list3.add_data(this_node.getdata()+this_node2.getdata())
        this_node = this_node.getnext()
        this_node2 = this_node2.getnext()
    return(list3)
list3 = addTwoNumbers(list1, list2)
i = 0
this_node = list3.root
while this_node:
    print(this_node.getdata())
    this_node = this_node.getnext()

        
        
        
        
