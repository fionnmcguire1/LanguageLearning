"""
Author: Fionn Mcguire
Date: 22-09-2017
Description: Check if a number is duplcated in a sorted list, remove duplicates and return the new size
"""

sorted_ary = [1,1,2,4,5,34,45,66,66,78,89,99,99,100,100,100,100]
def RemoveDuplicates(sorted_ary):
    index = 0
    while index < (len(sorted_ary)-1):
        if sorted_ary[index] == sorted_ary[index+1] :
            del sorted_ary[index+1]
            index -=1
        index+=1
    return(len(sorted_ary))

print(sorted_ary)
print(RemoveDuplicates(sorted_ary))
print(sorted_ary)


        
