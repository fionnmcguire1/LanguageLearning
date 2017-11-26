'''
Author: Fionn Mcguire
Date: 26-11-2017
Description: Check if int is palindrome
'''

class Solution(object):
        def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        str1=str(x)
        for index in xrange((len(str1)/2)):
            if str1[index] != str1[-index-1]:
                return False
        return True
