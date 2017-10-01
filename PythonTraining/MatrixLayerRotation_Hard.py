'''
Author: Fionn Mcguire
Date: 29-09-2017
Description: Rotate a 2d matrix x times each layer anticlockwise

Sample input:
4 4 2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16

Sample Output:
3 4 8 12
2 11 10 16
1 7 6 15
5 9 13 14
'''

n= input().split(' ')

ary = [[0 for i in range(int(n[0]))] for j in range(int(n[1]))]
a,b = 0
for i in range(int(n[1])):
    l = input().split(' ')
    for j in range(int(n[1])):
        ary[i][j] = l[j] 
for hello in range(int(n[2])):
    for i in range(int(n[1])):
        for j in range(int(n[1])):
            if j-1 == i:
                a+=1
            if j+1 == :
