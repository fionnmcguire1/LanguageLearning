'''
Author: Fionn Mcguire
Date: 29-11-2017
Description: A self-dividing number is a number that is divisible by every digit it contains.
For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
Also, a self-dividing number is not allowed to contain the digit zero.
Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.
'''


class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        returnList = []
        for i in xrange(left,right+1):
            str1 = str(i)
            checker = True
            for j in str1:
                if int(j) == 0 or i%int(j) != 0:
                    checker = False
                    break
            if checker == True:
                returnList.append(i)
        return returnList
