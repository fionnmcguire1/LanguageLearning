def mergeSort(arr):
    if len(arr) >1:
        mid = len(arr)//2 #Double slash floors the middle
        L = arr[:mid]
        R = arr[mid:]

        L = mergeSort(L) # Sorting the first half
        R = mergeSort(R) # Sorting the second half

        left_index = right_index = new_arr_index = 0
        length_of_left = len(L)
        length_of_right = len(R)

        while left_index < length_of_left and right_index < length_of_right:
            if L[left_index] < R[right_index]:
                arr[new_arr_index] = L[left_index]
                left_index+=1
            else:
                arr[new_arr_index] = R[right_index]
                right_index+=1
            new_arr_index+=1

        # Check if any element was left
        while left_index < len(L):
            arr[new_arr_index] = L[left_index]
            left_index+=1
            new_arr_index+=1

        while right_index < len(R):
            arr[new_arr_index] = R[right_index]
            right_index+=1
            new_arr_index+=1

    return arr



arr = mergeSort([0,5,4,35,6,6543,32,53,3])
print(arr)
