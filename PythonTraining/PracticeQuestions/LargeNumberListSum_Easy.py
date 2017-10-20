'''
Author: Fionn Mcguire
Date: 24-09-2017
Description: Function which computes the sum of a list of large numbers
'''
import sys

def aVeryBigSum(n, ar):
    # Complete this function
    bigNumberCounter = 0
    result = 0
    for i in ar:
        while i > 2**32:
            bigNumberCounter+=1
            i -= 2**32
        result+=i
    result+=(2**32)*bigNumberCounter
            
            
    return(result)
        

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = aVeryBigSum(n, ar)
print(result)
