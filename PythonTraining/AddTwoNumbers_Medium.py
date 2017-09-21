# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = []
        for index, i in l1:
            l3.append((l1[index]+l2[index])%10)
            
            
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

mylist = LinkedList()
mylist.add_data(5)
mylist.add_data(11)
mylist.add_data(17)
mylist.add_data(6)
mylist.add_data(8)
mylist.add_data(3)
mylist.add_data(34)
mylist.add_data(1)
mylist.remove(6)
print(mylist.remove(8))

    
                    
        
        
        
        
