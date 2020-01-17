'''
Author: Fionn Mcguire
Date: 21-09-2017
Description: Program to generate a staircase with hashtags.  
'''




import sys


n = int(input().strip())
a = ""
total = n+1

while n > 0:
    spaces = n-1
    hashtags = total-n
    a+=(" "*spaces)
    a+=("#"*hashtags)
    a+="\n"
    n-=1
print(a)


