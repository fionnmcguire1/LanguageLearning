'''
Author: Fionn Mcguire
Date: 09-10-2017
Description: Working with and manipulating various data structures

'''

def leftRotation(a, d):
    # Complete this function
    if d != 0:
        b = [0 for i in range(len(a))]
        for i in range(len(a)):
            c = (i-d)%(len(a))
            b[c] = a[i]
        str1 = ""
    else:
        b = a
    for i in range(len(b)):
        str1+=str(b[i])+" "
    return(b)

if __name__ == "__main__":
    n, d = input().strip().split(' ')
    n, d = [int(n), int(d)]
    a = list(map(int, input().strip().split(' ')))
    result = leftRotation(a, d)
    print (" ".join(map(str, result)))
