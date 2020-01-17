'''
Author: Fionn Mcguire
Date: 05-12-2017
Description: There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).


'''





class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        def GetMedian(list1):
            length1 = len(nums1)
            if length1 > 1:
                if (length1/2)%1 != 0:
                    med1 = length1//2
                else:
                    med1 = (nums1[int(length1/2)]+nums1[int((length1/2)-1)])/2
            else:
                med1 = 1     
            return med1
        
        med1,med2 = GetMedian(nums1),GetMedian(nums1)
        median = (med1 + med2) / 2
        return median
        
