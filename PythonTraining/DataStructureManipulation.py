'''
Author: Fionn Mcguire
Date: 09-10-2017
Description: Working with and manipulating various data structures

'''

def leftRotation(a, d):
    # Complete this function
    if d != 0:
        b = [0 for i in range(len(a))]
        for i in range(len(a)):
            c = (i-d)%(len(a))
            b[c] = a[i]
        str1 = ""
    else:
        b = a
    for i in range(len(b)):
        str1+=str(b[i])+" "
    return(b)
#Executes the leftRotation method
'''if __name__ == "__main__":
    n, d = input().strip().split(' ')
    n, d = [int(n), int(d)]
    a = list(map(int, input().strip().split(' ')))
    result = leftRotation(a, d)
    print (" ".join(map(str, result)))
'''

'''Rotation Matrix'''
#Rotate matrix m, n times
#Mode indicates whether the entire matrix moves 90 degrees
#or if the layers move in different directions
m = [[i for i in range(10)] for j in range(10)]
#Printing this easier to read with loop
#print(m)
for i in m:
    print(i)
class Node(object):
    def __init__(self,d,n = None,p = None):
        self.data = d
        self.next = n
        self.prev = p

class Linkedlist(object):
    def __init__(self,r = None):
        self.root = None
        self.size = 0
    def add(self,d):
        new_node = Node(d,self.root)
        if self.size > 0:
            next_node = new_node.next
            next_node.prev = new_node
        self.root = new_node
        self.size+=1

def RotateMatrix(m,n,mode):
    dimr = len(m)
    dimc = len(m[0])
    layer = 0
    numLayers = dimr//2
    arrOfLists = []

    list1 = Linkedlist()
    numOfCells = (2*dimr)+(2*dimc)-4
    Bottom = dimr-layer
    Right = (Bottom+(dimc-layer-2))
    Top = (Right+(dimr-layer))
    Left = (Top+(dimr-layer))

    for i in range(numOfCells):
        #BOTTOM
        if i in range(Bottom):
            val = m[layer][i]
            list1.add(val)
        #RIGHT
        elif i in range(Bottom,Right):
                val = m[i-dimr][dimr-1]
                list1.add(val)
            #TOP
        elif i in range(Right,Top):
                val = m[dimr-layer-1][(i-Right)*-1-1]
                list1.add(val)
            #LEFT
        elif i in range(Top,numOfCells):
                val = m[(i-Top)*-1][layer]
                list1.add(val)
    arrOfLists.append(list1)
    currentList = arrOfLists[0]
    currentNode = currentList.root
    while currentNode:
        print(currentNode.data)
        currentNode = currentNode.next
n = 10
mode = 0
RotateMatrix(m,n,mode)
