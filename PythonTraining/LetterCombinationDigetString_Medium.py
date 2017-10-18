'''
Author: Fionn Mcguire
Date: 18-10-2017
Description: Return all letter combinations of diget string
'''


digetString = "23"

lettergroups = ['%','abc','def','ghi','jkl','mno','pqrs','tuv','wzyz']

class Node(object):
    def __init__(self,d,child = None):
        self.data = d
        self.child = []
    def add(self,d):
        self.child.append(Node(d))

newnode = Node(lettergroups[0])
for i in range(1,len(lettergroups)):
    if i >1:
        newnode = 
    for j in lettergroups[i]:
        newnode.add(j)
