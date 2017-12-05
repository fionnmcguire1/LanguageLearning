'''
Author: Fionn Mcguire
Date: 05-11-2017
Description: Practicing Heaps
'''

#Implementation of heap using array
heap = []
def addToHeap(heap,data):
    length = len(heap)
    i = 0
    while i < length:
        if heap[i] <= data:
            heap.insert(i,data)
            return heap
        i+=1
    heap.append(data)
    return heap


def addToMinHeap(heap,data):
    heap.append(data)
    i = len(heap)-1
    while i > 0:
        if heap[i] < heap[i-1]:
            heap[i],heap[i-1] = heap[i-1],heap[i]
            i-=1
        else:
            break
    return heap


for i in range(20):
    heap = addToHeap(heap,i)
    


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
