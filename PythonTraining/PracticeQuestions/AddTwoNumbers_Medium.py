'''
Author: Fionn Mcguire
Date: 05-12-2017
Description: You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        
        def GetNum(currentNode):
            num = ''
            while currentNode:
                num+=str(currentNode.val)
                currentNode = currentNode.next
            return num
        num1,num2 = GetNum(l1),GetNum(l2)
        num1,num2 = num1[::-1],num2[::-1]
        num3 = int(num1)+int(num2)
        num3 = str(num3)
        num3 = num3[::-1]
        checker = False
        for i in num3:
            if checker == False:
                newNode = ListNode(i)
                firstNode = newNode
                checker = True
            else:
                newNode.next = ListNode(i)
                newNode = newNode.next
        return firstNode
