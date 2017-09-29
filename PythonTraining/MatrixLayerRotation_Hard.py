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

n= map(int,input().split(' '))

ary = [[0 for i in range(n[0])] for j in range(n[1])]

for i in range(n[1]):
    l = map(int,input().split(' '))
    for j in range(n[0]):
        colMove = n[2]-i
        if colMove < n[2]
        rowMove = 
        
'''
00,01,02,03,04,05
10,11,12,13,14,15
20,21,22,23,24,25
30,31,32,33,34,35
40,41,42,43,44,45
'''
