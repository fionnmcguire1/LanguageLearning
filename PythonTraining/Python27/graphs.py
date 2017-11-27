'''
Author: Fionn Mcguire
Date: 27-11-2017
Description: Practicing graphs and graph search algorithms
'''



class Node():
    def __init__(self,d):
        self.data = d
        self.children = []

    def addChild(self,c=None):
        self.children.append(c)

class Graph():
    def __init__(self):
        self.head = None

    def DepthFirstSearch(self,d):
        rootNode = self.head
        if rootNode.data == d:
            return True
        
        def hasPath(checked,children,d):
            for child in children:
                if child not in checked:
                    if child.data == d:
                        return True
                    checked.append(child)
                    answer = hasPath(checked,child.children,d)
                    if answer == True:
                        return True

        checked = []
        checked.append(rootNode)

        if hasPath(checked,rootNode.children,d) == True:
            return True
        return False

    def BreathFirstSearch(self,d):
        rootNode = self.head
        if rootNode.data == d:
            return True
        checkingNodes = []
        checkingNodes+=rootNode.children
        checked = []
        def checkLayer(checked,checkingNodes,d):
            newCheckingNodes = []
            for child in checkingNodes:
                if child not in checked:
                    checked.append(child)
                    if child.data == d:
                        return True
                    newCheckingNodes += child.children
            answer = checkLayer(checked,newCheckingNodes,d)
            if answer == True:
                return True
            return False
newGraph = Graph()
newNode = Node(1)
newGraph.head = newNode
newNode.addChild(Node(2))
newNode.addChild(Node(3))
newNode.addChild(Node(4))
child = newNode.children[1]
child.addChild(Node(5))
child.addChild(Node(6))
child.addChild(Node(7))
child.addChild(newGraph.head)

print newGraph.BreathFirstSearch(4)
