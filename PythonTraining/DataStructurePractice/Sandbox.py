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

##############################################
####### ******************************** #####
####### ********** DSA_Stack *********** #####
####### ******************************** #####
##############################################

#Stack LIFO Last in first out
#
# stack = []
# stack.insert(0,0)
# stack.insert(0,1)
# stack.insert(0,2)
# stack.insert(0,3)
# stack.insert(0,4)
#
# stack.pop(0)
# print(stack)
#
#
#
#
# #Queue is FIFO First in First Out
# queue = []
#
# queue.append(0)
# queue.append(1)
# queue.append(2)
# queue.append(3)
# queue.append(4)
#
# queue.pop(0)
#
# print(queue)

from collections import defaultdict

def getSongPairCount(songs):
    print(songs)

    num_song_pairs_returned = 0
    formatted_song_lengths = defaultdict(int)
    song_duration_mod_list = []

    #Loading songs into dictionary %60 as this is the only data we need
    for song_duration in songs:
        song_duration_mod = song_duration%60
        song_duration_mod_list.append(song_duration_mod)
        formatted_song_lengths[song_duration_mod] +=1


    for song_duration in song_duration_mod_list:
        remainder_needed = 60-song_duration

        #This will look for 60 in the dict, we need to point it to 0
        if remainder_needed == 60:
            remainder_needed = 0
        try:
            if remainder_needed != song_duration and formatted_song_lengths[remainder_needed] >= 1 and formatted_song_lengths[song_duration] >= 1:
                num_song_pairs_returned +=1
            elif remainder_needed == song_duration and formatted_song_lengths[remainder_needed] >= 2:
                num_song_pairs_returned +=1
        except Exception as e:
            print(e)

    return num_song_pairs_returned




from collections import defaultdict

def getSongPairCount(songs):
    print(songs)

    num_song_pairs_returned = 0
    formatted_song_lengths = defaultdict(list)
    second_argument_song_list = defaultdict(list)
    song_duration_mod_list = []

    #Loading songs into dictionary %60 as this is the only data we need
    for index,song_duration in enumerate(songs):
        song_duration_mod = song_duration%60
        song_duration_mod_list.append(song_duration_mod)
        formatted_song_lengths[song_duration_mod].append(index)


    for index,song_duration in enumerate(song_duration_mod_list):
        remainder_needed = 60-song_duration

        #This will look for 60 in the dict, we need to point it to 0
        if remainder_needed == 60:
            remainder_needed = 0
        try:
            if remainder_needed != song_duration and formatted_song_lengths[remainder_needed] != [] and formatted_song_lengths[song_duration] != []:
                if index not in formatted_song_lengths[song_duration]:
                    num_song_pairs_returned +=1
            elif remainder_needed == song_duration and len(formatted_song_lengths[remainder_needed]) >= 2:
                if index not in formatted_song_lengths[remainder_needed]:
                    num_song_pairs_returned +=1
        except Exception as e:
            print(e)

    return num_song_pairs_returned


print(getSongPairCount([402, 352, 36, 564, 54, 595, 157, 748, 367, 339, 262, 667, 564, 963, 945, 650, 735, 168, 254, 186, 153, 113, 219, 976, 71, 17, 516, 147, 705, 129, 818, 954, 959, 928, 917, 639, 460, 741, 981, 360, 597, 976, 906, 955, 672, 926, 337, 519, 663, 332, 23, 431, 596, 865, 797, 583, 525, 366, 284, 863, 30, 806, 704, 469, 539, 56, 615, 349, 165, 106, 425, 434, 930, 293, 79, 899, 759, 573, 589, 721, 911, 600, 657, 933, 227, 484, 195, 996, 736, 82, 341, 468, 110, 919, 883, 118, 342, 952, 913, 308, 417, 59, 697, 9, 661, 442, 828, 390, 536, 184, 374, 377, 924, 491, 844, 389, 876, 58, 182, 470, 219, 423, 679, 547, 577, 796, 898, 757, 599, 231, 108, 148, 119, 791, 823, 262, 23, 510, 738, 617, 572, 110, 587, 942, 561, 814, 751, 142, 855, 749, 30, 438, 444, 259, 826, 588, 990, 972, 886, 281, 863, 654, 960, 470, 920, 415, 25, 489, 319, 2, 409, 551, 339, 16, 581, 281, 396, 417, 971, 937, 190, 747, 562, 523, 444, 6, 781, 494, 406, 224, 518, 923, 461, 764, 980, 786, 332, 571, 159, 609, 766, 597, 304, 550, 36, 862, 924, 850, 62, 83, 543, 966, 574, 380, 739, 758, 762, 538, 880, 146, 801, 591, 771, 322, 850, 178, 73, 71, 138, 186, 330, 879, 204, 1000, 184, 687, 144, 407, 759, 416, 134, 245, 925, 652, 354, 689, 816, 887, 375, 628, 524, 984, 518, 290, 341, 519, 774, 968, 694, 486, 691, 173, 290, 546, 504, 459, 537, 769, 406, 284, 127, 132, 741, 631, 106, 748, 152, 770, 419, 781, 163, 959, 977, 591, 358, 425, 659, 514, 752, 853, 100, 471, 86, 228, 22, 148, 259, 677, 362, 614, 264, 997, 388, 853, 387, 224, 121, 13, 353, 190, 425, 769, 445, 89, 87, 384, 752, 491, 598, 194, 345, 506, 435, 881, 204, 358, 743, 738, 901, 295, 588, 435, 235, 265, 629, 340, 487, 553, 368, 256, 404, 334, 949, 571, 750, 811, 421, 923, 669, 561, 997, 888, 225, 135, 378, 829, 725, 916, 213, 959, 781, 176, 526, 619, 738, 552, 435, 585, 162, 273, 719, 309, 970, 482, 413, 402, 838, 308, 500, 743, 285, 595, 57, 284, 599, 123, 778, 467, 984, 285, 367, 697, 204, 282, 521, 91, 698, 588, 797, 956, 420, 489, 880, 195, 555, 233, 137, 959, 268, 269, 651, 581, 191, 920, 306, 373, 348, 487, 3, 554, 814, 730, 606, 992, 594, 498, 173, 622, 694, 867, 84, 508, 660, 857, 256, 803, 950, 4, 730, 561, 849, 766, 139, 44, 756, 457, 223, 548, 559, 811, 428, 611, 118, 323, 290, 510, 502, 459, 66, 658, 84, 909, 328, 505, 899, 136, 938, 773, 28, 707, 968, 521, 532, 302, 220, 453, 467, 717, 809, 200, 49, 782, 46, 853, 738, 311, 978, 184, 633, 963, 527, 664, 677, 76, 640, 540, 528, 119, 804, 880, 620, 277, 827, 639, 486, 334, 573, 200, 533, 61, 344, 314, 226, 433, 944, 497]))
