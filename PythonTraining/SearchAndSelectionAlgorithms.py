'''
Author: Fionn Mcguire
Date: 16-09-2017
Description:
    Search and selection algorithms
'''

#unordered list
sample_dataset = [0,1,2,3,6,7,5,4,56,765,32,45,98,-22,4,5,-456,1,8,88,-11,-0]

#ordered list
sample_dataset_ordered = [0,1,4,7,9,44,66,77,87,98,100]


#find min
def findmin (sample_dataset):
    i = 0
    while i < len(sample_dataset):
        if i == 0:
            temp = sample_dataset[i]
        else:
            if sample_dataset[i] < temp:
                temp = sample_dataset[i]
        i+=1
    return temp
'''
min_num = findmin(sample_dataset)
print(min_num)
min_num = findmin(sample_dataset_ordered)
print(min_num)
print(max(sample_dataset))'''

#Use binary search to efficiently return the position of a value within
#a sorted list. This is particularly efficient with large sorted lists. The algorithm defaults to
# return a message Not found but can easily be altered to return an integer or null value as
#to not mess with the rest of a program which may be utilizing this method
def BinarySearch(arr,value):
    lowIndex = 1
    highIndex = len(arr)
    while lowIndex <= highIndex and (highIndex - lowIndex) > 1:        
        middle = int(round((highIndex + lowIndex)/2))
        if arr[middle] == value:
            return middle
        elif arr[middle] > value:
            highIndex = middle
        elif arr[middle] < value:
            lowIndex = middle
    return "Not found"
'''num = BinarySearch(sample_dataset_ordered,112)
print(num)'''


def partition(array, begin, end):
    pivot = begin
    for i in range(begin+1, end+1):
        if array[i] <= array[begin]:
            pivot += 1
            array[i], array[pivot] = array[pivot], array[i]
    array[pivot], array[begin] = array[begin], array[pivot]
    return pivot



def quicksort(array, begin=0, end=None):
    if end is None:
        end = len(array) - 1
    def _quicksort(array, begin, end):
        if begin >= end:
            return
        pivot = partition(array, begin, end)
        _quicksort(array, begin, pivot-1)
        _quicksort(array, pivot+1, end)
    return _quicksort(array, begin, end)

print(sample_dataset)
quicksort(sample_dataset)
print(sample_dataset)
