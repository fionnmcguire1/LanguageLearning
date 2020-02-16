
class GraphNode(object):
    def __init__(self,value):
        self.value = value
        self.neigbours = []

class Graph(object):

    def __init__(self):
        self.hashmap = dict()

    def addNode(self,value):
        self.hashmap[value] = GraphNode(value)

    def addNeigbour(self,node_value,new_neigbour):
        current_node = self.hashmap[node_value]
        current_node.neigbours.append(self.hashmap[new_neigbour])

    def traverseGraph(self):
        for node in self.hashmap.keys():
            print("Node: ",self.hashmap[node].value)
            print("Neigbours: ",self.hashmap[node].neigbours)

    def checkPath(self,start_node,end_node):
        start = self.hashmap[start_node]
        end = self.hashmap[end_node]
        if start == end: return True
        while True:
            if end in start.neigbours:
                return True
            else:
                if start.neigbours == []: return False
                start = start.neigbours[0]

    def validateAlienString(self,string):
        if len(string) <= 1: return True
        length_of_string = len(string)
        for index,letter in enumerate(string):
            if index+1 != length_of_string and self.checkPath(letter,string[index+1]) == False:
                return False
        return True

#Alien Dictionary
# B -> F -> G -> Q
#        -> L -> B
#
#
alien_dictionary = ['b','f','g','q']
length_of_alien_dictionary = len(alien_dictionary)
graph_instance = Graph()
for letter in alien_dictionary:
    graph_instance.addNode(letter)

for index,letter in enumerate(alien_dictionary):
    if index+1 != length_of_alien_dictionary:
         graph_instance.addNeigbour(letter,alien_dictionary[index+1])

graph_instance.traverseGraph()
alien_words = ["bgg","fbq","fqf","ffq","gfg"]
for word in alien_words:
    print(word+": ",graph_instance.validateAlienString(word))
