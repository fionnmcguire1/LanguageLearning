'''
Author: Fionn Mcguire
Date: 28-11-2017
Description: To split a linked list into two.
'''
def SplitLinkedList(root, k):
    counter = 0
    currentNode = root
    while currentNode:
        counter+=1
        currentNode = currentNode.next
        
    SplitLength = counter//k
    remainder = counter%k
        
    currentNode = root
    LinkedList = []
    counter = 0
    ReturnedList
    checker = True
    while currentNode:
        LinkedList+=currentNode
        if len(LinkedList)%SplitLength == 0 and remainder == 0 and checker == True:
            ReturnedList.append(LinkedList)
            checker = False
        else if len(LinkedList)%SplitLength == 1 and remainder > 0:
            remainder -=1
            checker = True
        currentNode = currentNode.next
    return ReturnedList
