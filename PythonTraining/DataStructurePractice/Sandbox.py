##############################################
####### ******************************** #####
####### ******** DSA_BinaryTree ******** #####
####### ******************************** #####
##############################################

class BinaryNode(object):
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val

class BinaryTree(object):
    def __init__(self):
        self.root = None

    def addNode(self,value):
        if self.root is None:
            self.root = BinaryNode(value)
        else:
            current_node = self.root
            while True:
                if current_node.val >= value:
                    if current_node.left is None:
                        current_node.left = BinaryNode(value)
                        break
                    else:
                        current_node = current_node.left
                else:
                    if current_node.right is None:
                        current_node.right = BinaryNode(value)
                        break
                    else:
                        current_node = current_node.right


    #Left to right
    def inOrderPrint(self,current_node=None):
        if current_node is None:
            current_node = self.root

        if current_node.left is not None:
            self.inOrderPrint(current_node.left)

        print(current_node.val)

        if current_node.right is not None:
            self.inOrderPrint(current_node.right)

    #Root gets printed first then left then right
    def preOrderPrint(self,current_node=None):
        if current_node is None:
            current_node = self.root

        print(current_node.val)

        if current_node.left is not None:
            self.preOrderPrint(current_node.left)

        if current_node.right is not None:
            self.preOrderPrint(current_node.right)

    def postOrderPrint(self,current_node=None):
        if current_node is None:
            current_node = self.root

        if current_node.left is not None:
            self.postOrderPrint(current_node.left)

        if current_node.right is not None:
            self.postOrderPrint(current_node.right)

        print(current_node.val)


##############################################
## Testing Binary Tree Different Traversals ##
##############################################

# new_tree = BinaryTree()
#
# random_list = [4,7,56,34,2,52,12,1,1,6,7,865,0]
#
# for i in random_list:
#     new_tree.addNode(i)
#
# print("In")
# new_tree.inOrderPrint()
# print("Pre")
# new_tree.preOrderPrint()
# print("Post")
# new_tree.postOrderPrint()

##############################################
####### ******************************** #####
####### *********** DSA_Graph ********** #####
####### ******************************** #####
##############################################


#Dictionary based graph
new_graph = {}

def addNode(graph,val):
    if val in graph.keys():
        return
    else:
        new_graph[val] = []

def addEdge(graph,node,path_node):
    try:
        if path_node in graph[node]:
            return
        else:
            graph[node].append(path_node)
    except:
        pass

def graphDFS(graph,source,dest,visited=None):
    if visited is None:
        visited = [source]
    if source == dest:
        print(visited)
    else:
        for node in graph[source]:
            if node not in visited:
                graphDFS(graph,node,dest,visited+[node])

def graphBFS(graph,source,dest,visited=None):
    if visited is None:
        visited = [source]
    if source == dest:
        print(visited)
    elif dest in graph[source]:
        visited.append(dest)
        print(visited)
    else:
        for node in graph[source]:
            if node not in visited:
                graphBFS(graph,node,dest,visited+[node])


addNode(new_graph,"A")
addNode(new_graph,"B")
addNode(new_graph,"C")
addNode(new_graph,"D")
addNode(new_graph,"E")
addNode(new_graph,"F")
addNode(new_graph,"G")
addNode(new_graph,"H")
addNode(new_graph,"I")

addEdge(new_graph,"A","B")
addEdge(new_graph,"A","C")
addEdge(new_graph,"A","D")
addEdge(new_graph,"B","D")
addEdge(new_graph,"B","I")
addEdge(new_graph,"B","H")
addEdge(new_graph,"H","G")

# print("Path")
# graphDFS(new_graph,"A","G")
# graphDFS(new_graph,"B","G")
# print("No Path")
# graphDFS(new_graph,"H","A")
#
# print("Path")
# graphBFS(new_graph,"A","G")
# graphBFS(new_graph,"B","G")
# print("No Path")
# graphBFS(new_graph,"H","A")


#Object based Graph
class Graph(object):
    def __init__(self):
        self.nodes = {}

    def addNodeToGraph(self,val):
        if val not in self.nodes.keys():
            self.nodes[val] = []

    def addEdge(self,parent,child):
        if child not in self.nodes[parent]:
            self.nodes[parent].append(child)

    def depthFirstSearch(self,source,dest,visited=None):
        if visited is None:
            visited = [source]
        if source == dest:
            print(visited)
        else:
            for node in self.nodes[source]:
                if node not in visited:
                    self.depthFirstSearch(node,dest,visited+[node])

new_graph = Graph()
nodes = "ABCDEFGHIJK"
for letter in nodes:
    new_graph.addNodeToGraph(letter)

new_graph.addEdge("A","B")
new_graph.addEdge("B","C")
new_graph.addEdge("C","D")
new_graph.addEdge("B","E")
new_graph.addEdge("B","H")
new_graph.addEdge("H","I")
new_graph.addEdge("J","K")
new_graph.addEdge("K","B")
new_graph.addEdge("K","A")
new_graph.addEdge("K","A")
new_graph.addEdge("K","K")


#print("Paths found For obj")
#print(new_graph.depthFirstSearch("A","H"))


##############################################
####### ******************************** #####
####### *********** DSA_Trie *********** #####
####### ******************************** #####
##############################################

class Node(object):
    def __init__(self,val):
        self.val = val
        self.children = []

class Trie(object):
    def __init__(self):
        self.root_nodes = []

    def addWord(self,word):
        current_node = None
        for letter in word:
            if current_node is None:
                for node in self.root_nodes:
                    if letter == node.val:
                        current_node = node
                        break
                current_node = Node(letter)
                self.root_nodes.append(current_node)
            else:
                for node in current_node.children:
                    if node.val == letter:
                        current_node = node
                        break
                new_node = Node(letter)
                current_node.children.append(new_node)
                current_node = new_node

    def findWord(self,word,current_node=None):
        for letter in word:

            if current_node is None:
                looping_nodes = self.root_nodes
            else:
                looping_nodes = current_node.children

            for node in looping_nodes:
                if node.val == letter:
                    if len(word) >1:
                        return self.findWord(word[1:],node)
                    else:
                        return True
        return False



# new_trie = Trie()
# new_trie.addWord("letter")
# print(new_trie.findWord("letter"))

########################################
#### Different Trie Implementation #####
########################################

class Node(object):
    def __init__(self,is_complete_word=False):
        self.children = {}

class Trie(object):

    def __init__(self):
        self.root = Node()

    def addWord(self,word,current_node=None):
        if current_node is None:
            current_node = self.root

        try:
            if word[0] in current_node.children.keys():
                next_node = current_node.children[word[0]]
            else:
                next_node = Node()
                current_node.children[word[0]] = next_node

            self.addWord(word=word[1:],current_node=next_node)
        except:
            return


    def findWord(self,word,current_node=None):
        if current_node is None:
             current_node = self.root

        if word[0] in current_node.children.keys():
            try:
                return self.findWord(word[1:], current_node.children[word[0]])
            except:
                return True
        else:
            return False



#Adding Words
new_trie = Trie()
new_trie.addWord("letter")
new_trie.addWord("long")
new_trie.addWord("laughter")

#Finding words
# print("Find Words")
# print(new_trie.findWord("letter"))
# print(new_trie.findWord("lx"))

##############################################
####### ******************************** #####
####### ******** DSA_LinkedList ******** #####
####### ******************************** #####
##############################################


class Node(object):
    def __init__(self,val):
        self.val = val
        self.prev = None
        self.next = None


class LinkedList(object):
    def __init__(self):
        self.root = None
        self.tail = None


    def addNode(self,val):

        new_node = Node(val)

        if self.root is None:
            self.root = new_node
            self.tail = new_node
            self.tail.prev = new_node

        else:
            new_node.next = self.root
            self.root.prev = new_node
            self.root = new_node

    def traverseLinkedList(self):
        current_node = self.root
        while current_node is not None:
            print(current_node.val)
            current_node = current_node.next

    def printReverseLinkedList(self):
        current_node = self.tail
        while current_node is not None:
            print(current_node.val)
            current_node = current_node.prev


    def deleteNode(self,val):
        current_node = self.root
        while current_node is not None:
            if current_node.val == val:
                if current_node == self.root:
                    if current_node.next:
                        self.root = current_node.next
                    else:
                        self.root = None

                    break

                if current_node == self.tail:
                    if self.tail.prev:
                        self.tail.prev.next = None
                        self.tail = self.tail.prev

                    else:
                        self.tail = None
                else:

                    current_node.prev.next = current_node.next
                    current_node.next.prev = current_node.prev
                break
            else:
                current_node = current_node.next



new_linked_list = LinkedList()
new_linked_list.addNode(1)
new_linked_list.addNode(2)
new_linked_list.addNode(3)
new_linked_list.addNode(4)
new_linked_list.addNode(5)

#Testing out different ways of manipulating a linked list
# new_linked_list.traverseLinkedList()
# print("Deleted")
# new_linked_list.deleteNode(3)
# new_linked_list.deleteNode(2)
# print(new_linked_list.root.val)
# print(new_linked_list.tail.val)
# new_linked_list.deleteNode(5)
# new_linked_list.deleteNode(1)
# new_linked_list.deleteNode(4)
#
# new_linked_list.traverseLinkedList()
