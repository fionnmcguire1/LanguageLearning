'''
Quicksort algorithm:
Never asked to implement in real life but is a good algorithm to understand.
This operates on the premis of picking a value in the unsorted list
stepping the indexes from the outside toward the center.
If the value at the left index is greater than the pivot, it is held
If the value at the right index is less than the pivot, it is held
Once we have a value for the left and right, a swap is performed where
they are compared against each other. When the indexes reach the middle,
the quicksort is then performed on the left side of the middle and the
right side of the middle. This pattern continues multiple times until the
list is eventually sorted.
If one was to pick the pivot randomly and it was always the the first
element of the list, the time complexity would be n^2
The average case is O(log n)
Note: Pythons `sorted` is based off a modification of a quicksort algorithm


'''


def quicksort(unsorted_list):

    def _quicksort(left=0,right=None,unsorted_list=[]):

        #If the sort has been complete return nothing
        if right == None: right = len(unsorted_list)-1
        elif right <= left: return

        #Get partition actually performs the step through
        #And the swaps, returning the final index
        #The quick sort is then applied to each half.
        #As this happens recursively, the partitions break up over time

        unsorted_list,index = get_partition(left,right,unsorted_list)
        _quicksort(index,right,unsorted_list)
        _quicksort(left,index-1,unsorted_list)

    #No validation here, just a simple swap
    def swap(left,right,unsorted_list):
        left_value = unsorted_list[left]
        unsorted_list[left] = unsorted_list[right]
        unsorted_list[right] = left_value
        return unsorted_list

    def get_partition(left,right,unsorted_list=[]):
        #Pick the middle index as a pivot
        pivot = unsorted_list[int((left+right)/2)]


        while left < right:
            while unsorted_list[left] < pivot: left+=1
            while unsorted_list[right] > pivot: right-=1

            if unsorted_list[left] >= unsorted_list[right]:
                unsorted_list= swap(left,right,unsorted_list)
                left+=1
                right-=1
        return unsorted_list,left

    _quicksort(0,None,unsorted_list)
    print(unsorted_list)
    return unsorted_list


unsorted_list = [1,6,34,5,67,8,6,42,11,4,6,13,32,364,22]
print(unsorted_list)
quicksort(unsorted_list)
