def quicksort(unsorted_list):

    def _quicksort(left=0,right=None,unsorted_list=[]):
        if right == None: right = len(unsorted_list)-1
        elif right <= left: return


        unsorted_list,index = get_partition(left,right,unsorted_list)
        _quicksort(index,right,unsorted_list)
        _quicksort(left,index-1,unsorted_list)

    def swap(left,right,unsorted_list):
        left_value = unsorted_list[left]
        unsorted_list[left] = unsorted_list[right]
        unsorted_list[right] = left_value
        return unsorted_list

    def get_partition(left,right,unsorted_list=[]):
        pivot = unsorted_list[int((left+right)/2)]

        while left < right:
            while unsorted_list[left] < pivot:
                left+=1
            while unsorted_list[right] > pivot:
                right-=1

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
