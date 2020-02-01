'''
Expirmenting with a modified Trie data structure to
solve a combination problem

'''
class Node(object):
    def __init__(self,value,is_complete=False):
        self.value = value
        self.is_complete = is_complete
        self.children = []

class Trie(object):
    def __init__(self):
        self.root = []

    def add_root(self,value):
        self.root.append(Node(value))

    def add_node(self,limit,value,list_of_child_nodes=None,complete=False):
        if list_of_child_nodes is None: list_of_child_nodes = self.root
        for node in list_of_child_nodes:
            if len(node.children) <= limit:

                if len(value) == 1: node.children.append(Node(value,is_complete=complete))
                else:
                    for n in value:
                        node.children.append(Node(n,is_complete=complete))
            else: self.add_node(value,node.children)


    def get_combo(self,children=None,new_combo="",combinations=[]):
        if children == None: children = self.root
        #Traverse through
        #Check if it's complete
        #If it is append combinations
        #Return combinations
        for node in children:
            if node.is_complete == True: combinations.append(new_combo+node.value)
            else: combinations = self.get_combo(node.children,str(new_combo)+str(node.value),combinations)
        return combinations

new_trie = Trie()

hash_map_alpha = dict()
hash_map_alpha["2"] = "abc"
hash_map_alpha["3"] = "def"
hash_map_alpha["4"] = "ghi"
hash_map_alpha["5"] = "jkl"
hash_map_alpha["6"] = "mno"
hash_map_alpha["7"] = "qrs"
hash_map_alpha["8"] = "tuv"
hash_map_alpha["9"] = "wxyz"

combinations = []

digits = "2324"

for index,digit in enumerate(digits):

    if index == len(digits)-1: complete = True
    else: complete = False
    if len(new_trie.root) == 0:
        for letter in hash_map_alpha[digit]:
            new_trie.add_root(letter)

    else:
        new_trie.add_node(len(hash_map_alpha[digit]), hash_map_alpha[digit],None,complete)

print(new_trie.root)

print new_trie.get_combo()
