'''
Author: Fionn Mcguire
Date: 24-09-2017
Description: Compute diagonal difference between the sum of the diagonals

'''


n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)
i,j = 0,0
left,right = 0,0
while i < n:
    left += a[i][i]
    right += a[i][(n-i)-1]
    i+=1
if left > right:
    print(left-right)
else:
    print(right-left)
