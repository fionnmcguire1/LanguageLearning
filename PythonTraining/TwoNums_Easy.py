'''
Author: Fionn Mcguire
Date 21-09-2017
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
Assuming that each input would have exactly one solution,
and the same element may not be used twice.
'''

def twoSum(nums, target):
        for indexi,i in enumerate(nums):
            for indexj,j in enumerate(nums):
                if indexi != indexj:
                    if (i+j) == target:
                        return(indexi,indexj)


nums = [2, 7, 11, 15]
target = 9
twoSum(nums, target)
