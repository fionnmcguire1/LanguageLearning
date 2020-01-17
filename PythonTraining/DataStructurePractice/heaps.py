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
print(mySortedList)

potentialBubbleSort(mySortedList,0)
potentialBubbleSort(mySortedList,2)
potentialBubbleSort(mySortedList,6)
potentialBubbleSort(mySortedList,9)
potentialBubbleSort(mySortedList,11)





#Implementation of a heap
