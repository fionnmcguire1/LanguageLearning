# Enter your code here. Read input from STDIN. Print output to STDOUT

#Perform the read input
#Create the list organised in a heap
#Heapify sort method

def Heaify(heap,val,mode=1):
    len_of_heap = len(heap)
    if mode == 3 and len_of_heap !=0:
        print(heap[0])
        return heap
    elif mode == 1:
        heap.append(val)
        current_index = len(heap)-1
        len_of_heap+=1
    elif mode == 2:
        current_index = heap.index(val)
        heap.remove(val)
        len_of_heap-=1
        if len_of_heap == 0:
            return heap
    else: return heap


    if len_of_heap == 1: return heap
    else:
        while True:
            parent_node = int((current_index)/2)
            left_child = (current_index*2)+1
            right_child = (current_index*2)+2

            if left_child >= len_of_heap: left_child,right_child = None,None
            elif right_child >= len_of_heap: right_child = None


            if parent_node < 0: parent_node = 0


            if heap[parent_node] > val:
                heap[current_index] = heap[parent_node]
                heap[parent_node] = val
                current_index = parent_node
            elif right_child is not None and heap[current_index] > heap[left_child]:
                heap[current_index] = heap[left_child]
                heap[left_child] = val
                current_index = left_child
            elif right_child is not None and heap[current_index] > heap[right_child]:
                heap[current_index] = heap[right_child]
                heap[right_child] = val
                current_index = right_child
            else:
                return heap



number_of_runs = int(input().strip())
heap = []
for i in range(number_of_runs):
    input_val = input().strip()
    if input_val == '3':
        n = 3
        k = 0
    else:
        n,k = input_val.split(' ')
    n = int(n)
    k = int(k)

    heap = Heaify(heap,k,int(n))
