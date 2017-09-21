'''
Author: Fionn Mcguire
Date: 21-09-2017
Description: To Reverse a number inputted to the function and return a 0 if the 32 bit int overflows
Added functionality to check if the nuber provided is a pallindrome
'''


def reverse(x):
    if x > 2**32:
        return 0
    y = str(x)
    z = ""
    i = len(y)
    while i > 0:
        z+=y[i-1]
        i-=1
    if z == y:
        print("{0} a pallindrome!".format(z))
    x = int(z)
    return(x)
num = reverse(1453)
print(num)
num = reverse(1001)



