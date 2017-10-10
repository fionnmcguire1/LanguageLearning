'''
Author: Fionn Mcguire
Date: 10-10-2017
Description String manipulation

'''

'''Print a Welcome Mat in givne dimmentions'''
N, M = map(int,input().split()) # More than 6 lines of code will result in 0 score. Blank lines are not counted.
for i in range(1,N,2):
    print ("{}{}{}".format("-"*(M//2-(i+(i//2))),".|."*((i)),"-"*(M//2-(i+(i//2)))))
print ("{}WELCOME{}".format("-"*N,"-"*N))
for i in range(N-2,-1,-2):
    print ("{}{}{}".format("-"*(M//2-(i+(i//2))),".|."*((i)),"-"*(M//2-(i+(i//2)))))
