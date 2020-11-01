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

print("Path")
graphDFS(new_graph,"A","G")
graphDFS(new_graph,"B","G")
print("No Path")
graphDFS(new_graph,"H","A")

print("Path")
graphBFS(new_graph,"A","G")
graphBFS(new_graph,"B","G")
print("No Path")
graphBFS(new_graph,"H","A")


#Object based Graph

















##############################################
####### ******************************** #####
####### *********** DSA_Trie *********** #####
####### ******************************** #####
##############################################
