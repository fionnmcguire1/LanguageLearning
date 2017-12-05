'''
Author: Fionn Mcguire
Date: 05-11-2017
Description: Practicing Heaps
'''

#Implementation of heap using array
heap = []
def addToHeap(heap,data,mode='max'):
    length = len(heap)
    i = 0
    if mode == 'max':
        while i < length:
            if heap[i] <= data:
                heap.insert(i,data)
                return heap
            i+=1
        heap.append(data)
        return heap
    else if mode == 'min':
        #The only difference here is the sign
        #Rather than having to run a check every time in 
        #The above loop, it's better to check once at the call
        #and reduce the total number of operations
        #This does however lead to duplicate code
        while i < length:
            if heap[i] >= data:
                heap.insert(i,data)
                return heap
            i+=1
        heap.append(data)
        return heap


#Populating heap with loop
for i in range(20):
    heap = addToHeap(heap,i)

#Mixing it up
heap = addToHeap(heap,5)
heap = addToHeap(heap,6)
heap = addToHeap(heap,7)
heap = addToHeap(heap,14)
heap = addToHeap(heap,27)
heap = addToHeap(heap,56)
heap = addToHeap(heap,26)
heap = addToHeap(heap,20)
heap = addToHeap(heap,54)
heap = addToHeap(heap,57)
heap = addToHeap(heap,1)
heap = addToHeap(heap,0)
heap = addToHeap(heap,18)

print(heap)
