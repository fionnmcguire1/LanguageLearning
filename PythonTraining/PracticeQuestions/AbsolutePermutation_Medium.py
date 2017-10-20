'''
Author: Fionn Mcguire
Date: 18-10-2017
Description: Absolute Permutation Hackerank

'''


t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    #Check logic here
    if n == 0 or n < k or k < 0 or (k > 0 and (n%k != 0 or (n/k)%2 != 0)):
        print(-1)
    else:
        newperm = ""
        if k*2 == 0:
            for i in range(1,n+1):
                newperm+=str(i)+" "
        else:
            for i in range(1,n,k*2):
                for j in range(k):
                    #Check this below
                    newperm+=str(i+k+j)+" "
                for j in range(k):
                    newperm+=str(i+j)+" "
        print(newperm)
