'''
Author: Fionn Mcguire
Date: 30-09-2017
Description: Return the largest pallindromic substr
'''







class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        Longest = 0
        if s != s[::-1]:            
            for i in range(len(s)):
                j = i+1
                for j in range(len(s)):
                    if s[i:j] == s[i:j][::-1]:
                        if len(s[i:j]) > Longest:
                            Longest = len(s[i:j])
                            pallindomicSubStr = s[i:j]
            return pallindomicSubStr
        else:
            return s
