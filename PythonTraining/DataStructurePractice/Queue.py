'''
Author: Fionn Mcguire
Date: 30-10-2017
Description: Practicing a queue
'''



class Node(object):
    def __init__ (self,d,n=None,p=None):
        self.data = d
        self.nextN = n
        self.prev = p

class Queue(object):
    def __init__ (self,s, h = None, t = None):
        self.head = h
        self.tail = t
        self.sizeLimit = s
        self.size = 0

    def add(self,d):
        newNode = Node(d)
        if self.head is None:
            self.head,self.tail = newNode,newNode
            self.size+=1
        else:
            currentNode = self.head
            self.head = newNode
            currentNode.prev= newNode
            newNode.nextN = currentNode
            self.size+=1
            if self.size > self.sizeLimit:
                tailNode = self.tail
                prevNode = tailNode.prev
                self.tail = prevNode
                prevNode.nextN = None
                self.size-=1

newQueue = Queue(15)

for i in range(1, 21):
    newQueue.add(i)
    #print(newQueue.size)
currentNode = newQueue.head
while currentNode:
    print(currentNode.data)
    currentNode = currentNode.nextN



