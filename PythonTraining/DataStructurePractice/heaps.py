'''
Author: Fionn Mcguire
Date January 2020

Notes on Heaps:
2 forms -min and max heaps
In a min heap the elements are all smaller than their children

---------- 2 --------------
------- 4 --- 8 -----------
-----9---7---10---9--------
-15-20-13-11-12-11-10-11---


To insert an element it always goes top to bottom
Left to right. If the element is in the wrong order. We can
Bubble the element up comparing it to it's parent.


This can be implememented in a few ways.
1: Similar to a linked list where you have a root
Then the node has a left and right node. And it can be
implemented that way.

This can also be stored in an array.
This makes it very compact as I presume it doesn't have to deal with
a load of class meta data. Seperately a list is much easier to
traverse through should you know what you're looking for. For example
to find the largest value you can just get the last element.

'''



#Note sure if i'm about to implement a bubble sort but here we go
#as an attempot before learning the implementation
def potentialBubbleSort(mySortedList,insertable_number):
    min = 0
    max = len(mySortedList)
    starting_max = max
    if starting_max == 0: mySortedList.append(insertable_number)
    elif max == 1:
        if mySortedList[0] <=insertable_number: mySortedList.insert(0,insertable_number)
        else: mySortedList.append(insertable_number)
    while starting_max == len(mySortedList):

        if min+1 == max:
            #print("Index: {} Value: {}".format(str(min),str(mySortedList[min])))
            if mySortedList[min] >= insertable_number:
                mySortedList.insert(min,insertable_number)
            else: mySortedList.insert(max,insertable_number)
            break
        middle = int(round((max-min)/2))+min
        if mySortedList[middle] > insertable_number:max = middle
        elif mySortedList[middle] == insertable_number:
            mySortedList.insert(middle,insertable_number)
            break
        else: min = middle
    print(mySortedList)


mySortedList = [1,3,4,5,7,8,10]
# print(mySortedList)
#
# potentialBubbleSort(mySortedList,0)
# potentialBubbleSort(mySortedList,2)
# potentialBubbleSort(mySortedList,6)
# potentialBubbleSort(mySortedList,9)
# potentialBubbleSort(mySortedList,11)


#Implementation of a heap
heap_list = []


#Method to insert
#Method to remove
#Method to bubble up or down
def bubbleUpOrDown(heap_list,value):
    index = len(heap_list)-1
    while True:
        if index == 0: break
        #Calculating surrounding indexs
        parent_index = int(round(((index-2)/2)))
        left_child = int((index*2)+1)
        right_child = int((index*2)+2)

        #If it's the root, this calc will return a negative
        if parent_index < 0: parent_index = 0

        #Setting left and right to none if their index has not been set yet
        #This may prove redundant as we may have a rule that the bubble only happens once
        if left_child > len(heap_list)-1: left_child,right_child=None,None
        elif right_child > len(heap_list)-1: right_child=None

        if left_child is not None and heap_list[index] > heap_list[left_child]:
            tmp_left = heap_list[left_child]
            heap_list[left_child] = heap_list[index]
            heap_list[index] = tmp_left
            index = left_child
        elif right_child is not None and heap_list[index] > heap_list[right_child]:
            tmp_right = heap_list[right_child]
            heap_list[right_child] = heap_list[index]
            heap_list[index] = tmp_right
            index = left_child
        elif heap_list[index] < heap_list[parent_index]:
            tmp_parent = heap_list[parent_index]
            heap_list[parent_index] = heap_list[index]
            heap_list[index] = tmp_parent
            index = parent_index
        else:
            break
    return heap_list



def insertToHeap(heap_list,value):
    heap_list.append(value)
    heap_list = bubbleUpOrDown(heap_list,value)
    print(heap_list)


insertToHeap(heap_list,8)
insertToHeap(heap_list,9)
insertToHeap(heap_list,7)
insertToHeap(heap_list,10)
insertToHeap(heap_list,5)
insertToHeap(heap_list,20)
insertToHeap(heap_list,4)
insertToHeap(heap_list,2)
insertToHeap(heap_list,13)
insertToHeap(heap_list,32)
