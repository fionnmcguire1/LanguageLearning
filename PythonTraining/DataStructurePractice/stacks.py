
''' 
Author: Fionn Mcguire
Date: 30-10-2017
Description: Stack practice
'''

class Node(object):
	def __init__(self,d,n = None):
		self.data = d
		self.nextN = n

class Stack(object):
	def __init__(self,r = None):
		self.root = r
		self.size = 0

	def push(self,d):
		newNode = Node(d,self.root)
		self.root = newNode
		self.size+=1
	def pop(self):
		currentRoot = self.root
		self.root = currentRoot.nextN
		self.size-=1

newStack = Stack()
for i in range(20):
	newStack.push(i**i)
newStack.pop()
newStack.pop()
currentNode = newStack.root
while currentNode:
	print(currentNode.data)
	currentNode = currentNode.nextN
