#Trees and Graphs

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



new_tree = BinaryTree()

random_list = [4,7,56,34,2,52,12,1,1,6,7,865,0]
# Soreted random list = [0,1,1,2,4,6,7,7,12,34,52,56,865] for reference on result

for i in random_list:
    new_tree.addNode(i)

print("In")
new_tree.inOrderPrint()
print("Pre")
new_tree.preOrderPrint()
print("Post")
new_tree.postOrderPrint()
