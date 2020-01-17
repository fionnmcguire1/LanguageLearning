'''
Author: Fionn Mcguire
Date: 18-10-2017
Description: The grid search is designed to find a 2D array pattern within a larger 2D array

'''

import sys


t = int(input().strip())
for a0 in range(t):
    R,C = input().strip().split(' ')
    R,C = [int(R),int(C)]
    G = []
    G_i = 0
    for G_i in range(R):
       G_t = str(input().strip())
       G.append(G_t)
    r,c = input().strip().split(' ')
    r,c = [int(r),int(c)]
    P = []
    P_i = 0
    for P_i in range(r):
       P_t = str(input().strip())
       P.append(P_t)
    if R > r and C > c:
        for i in range(R-r):
            for j in range(C-c):
                k = 0
                for l in range(r):
                    if G[i][j:j+c] != P[l]:
                        l = 0
                        break
                    else:
                        i+=1
                if l+1 == r:
                    print("YES")
                    break
            if l+1 == r:
                break
        if l+1 != r:
            print("NO")
    elif G == P:
        print("YES")
    else:
        print("NO")
