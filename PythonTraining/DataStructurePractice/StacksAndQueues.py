class Node(object):
    def __init__(self,value):
        self.prev = None
        self.next = None
        self.value = value


class Stack(object):
    def __init__(self):
        self.tail = None
    def addValue(self,val):
        new_node = Node(val)
        if self.tail == None:
            self.tail = new_node
        else:
            self.tail.next = new_node
            temp_tail_node = self.tail
            self.tail = new_node
            self.tail.prev = temp_tail_node

    def removeValue(self):
        if self.tail is not None:
            self.tail = self.tail.prev

    def demonstrateValues(self):
        if self.tail is not None:
            while self.tail is not None:
                print(self.tail.value)
                self.tail = self.tail.prev

#I've just done a reversed linked list
class Queue(object):
    def __init__(self):
        self.head = None
        self.tail = None
    def addValue(self,val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            new_node = Node(val)
            if self.head == self.tail:
                self.head.next = new_node
                new_node.prev = self.tail
                self.tail = new_node
            else:
                new_node.prev = self.tail
                self.tail.next = new_node
                self.tail = new_node


    def removeValue(self):
        if self.head is not None: self.head = self.head.next


    def demonstrateValues(self):
        if self.head is not None:
            while self.head is not None:
                print(self.head.value)
                self.head = self.head.next

print("The big Stack")
thebigS = Stack()
for i in range(10):
    thebigS.addValue(i)
thebigS.demonstrateValues()
for i in range(10):thebigS.removeValue()

print("The big Queue")
thebigS = Queue()
for i in range(10):
    thebigS.addValue(i)
thebigS.demonstrateValues()
for i in range(10):thebigS.removeValue()
