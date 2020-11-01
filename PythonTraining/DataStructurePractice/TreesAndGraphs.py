'''
Author: Fionn Mcguire
Date: 13-10-2017
Description: Trees and graphs
'''

#Tree node
class Node(object):
    def __init__(self,d):
        self.data = d
        self.childleft = None
        self.childright = None
    def insert(self,d):
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
    def contains(self,d):
        if d == self.data:
            #print("Looking at: {} for {}".format(self.data,d))
            return True
        else:
            if d > self.data:
                if self.childleft:
                    return self.childleft.contains(d)
            else:
                if self.childright:
                    return self.childright.contains(d)
            return False



NewNode = Node(8)
NewNode.insert(7)
NewNode.insert(6)
NewNode.insert(4)
NewNode.insert(9)
NewNode.insert(10)
NewNode.insert(11)
NewNode.insert(14)
NewNode.insert(18)
NewNode.insert(19)
NewNode.insert(32)
NewNode.insert(55)
NewNode.insert(59)
NewNode.insert(62)
NewNode.insert(81)

print(NewNode.contains(14))
print(NewNode.contains(4))
print(NewNode.contains(19))
print(NewNode.contains(8))
print(NewNode.contains(18))
print(NewNode.contains(0))
print(NewNode.contains(1999999))

#TTTTTFF

class Trie(object):
    def __init__(self,d=None):
        self.data = None
        self.childNodes = []
    def addNode(self,dataset):
        for d in dataset:
            newNode = Trie(d)
            self.childNodes.append(newNode)




new_tree = dict()
new_tree['A'] = ['B','C']
new_tree['B'] =['D','E']
new_tree['D'] = ['F','E']
new_tree['F'] = ['D','E']
new_tree['E'] = ['D','B','C']
new_tree['C'] = ['A','E']

def traverse_tree(new_tree,visited=[]):
    if visited == []:
        current_node = list(new_tree.keys())[0]
        print(current_node)
        traverse_tree(new_tree,[current_node])
    else:
        for node in new_tree[visited[-1]]:
            if node in visited:
                pass
            else:
                print(node)
                visited.append(node)
                traverse_tree(new_tree,visited)

print("Traverse a Tree")
traverse_tree(new_tree)
