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

#Implement quicksort algorithm to sort a list in ascending order
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
'''
print(sample_dataset)
quicksort(sample_dataset)
print(sample_dataset)'''

#Second sorted list
arr = [63,65,78,91,92,93,95,97]
#arr1 = [0,1,2,3,4,5]
'''
arr+=arr1
arr1.append(6)
print(arr)
print(arr1)
'''

array = []
array2 = []
for i in range(500):
    array.append(i)
    array2.append(i+500)

def mergeSort(arr1,arr2):
    counter1 = 0
    counter2 = 0
    arr3 = []
    if len(arr1) > 0 and len(arr2) > 0:
        while 1:
            if counter1 >= len(arr1) or counter2 >= len(arr2):
                arr3+=(arr2[counter2:]+arr1[counter1:])
                break
            if arr1[counter1] < arr2[counter2]:
                arr3.append(arr1[counter1])
                counter1+=1
            else:
                arr3.append(arr2[counter2])
                counter2+=1
        return arr3
    else:
        arr3+=(arr1+arr2)
        return arr3

array3 = [0,1,2,3,4]
array4 = [3]
print(mergeSort(array3,array4))

'''
Find duplicate if there are characters in string
'''

def DuplicateChar(s):
    try:
        s = str(s)
    except ValueError:
        return "Data entered in method \"DucplicateChar\" was inconsistant with the data type allowed\n"+ValueError
    length = len(s)
    if length > 0:
        s =''.join(sorted(s))
        for i in range(length-1):
            if s[i] == s[i+1]:
                return True
    return False


string = "Hello"
string2 = "Mcguire"
string3 = 456789

#print(DuplicateChar(string))
#print(DuplicateChar(string2))
#print(DuplicateChar(string3))

def checkPermutation(s1,s2):
    try:
        s1 = str(s1)
        s2 = str(s2)
    except ValueError:
        return "Data entered in method \"DucplicateChar\" was inconsistant with the data type allowed\n"+ValueError

    len1 = len(s1)
    len2 = len(s2)
    if len1 == len2:
        if sorted(s1) == sorted(s2):
            return True
    return False

string = "Hello"
string2 = "Mcguire"
string3 = 456789
string4 = 547896

print(checkPermutation(string,string2))
print(checkPermutation(string3,string4))
print(checkPermutation(string,string4))
print(checkPermutation(string3,string2))
