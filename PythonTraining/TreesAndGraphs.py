'''
Author: Fionn Mcguire
Date: 13-10-2017
Description: Trees and graphs
'''


class Node(object):
    def __init__(self,d):
        self.data = None
        self.childleft = None
        self.childright = None
    def insert(d):
        if d >= self.data:
            if self.childleft == None:
                self.childleft = Node(d)
            else:
                self.childleft.insert(d)

        else:
            if self.childright == None:
                self.childright = Node(d)
            else:
                self.childright.insert(d)

NewNode = Node(8)
Node.insert(9)
Node.insert(19)
Node.insert(59)
Node.insert(4)
Node.insert(6)
Node.insert(7)
Node.insert(14)
Node.insert(11)
Node.insert(62)
Node.insert(81)
Node.insert(55)
Node.insert(32)
Node.insert(18)
Node.insert(19)
Node.insert(10)
