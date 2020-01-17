'''
Author: Fionn Mcguire
Date: 25-09-2017
Description:
    Emas Supercomputer Hackerank
'''
n,m = input().strip().split(' ')
n,m = [int(n),int(m)]

def checkCells(ary,middle,numCells):
    if ary[middle[0]+numCells][middle[1]] == 'G':
        if ary[middle[0]-numCells][middle[1]] == 'G':
            if ary[middle[0]][middle[1]+numCells] == 'G':
                if ary[middle[0]][middle[1]-numCells] == 'G':
                    return [(middle[0]+numCells,middle[1]),(middle[0]-numCells,middle[1]),(middle[0],middle[1]+numCells),(middle[0],middle[1]-numCells)]
    return []

def middleLayerIterator(aryOfGandB,rows,cols):
    checker = False
    aryOfPlusLocals = []
    #counter
    pluses = [0,0]
    for i in range(1,rows-1):
        for j in range(1,cols-1):
            if checker == False:
                if aryOfGandB[i][j] != 'B':
                    k = 1
                    temparyOfPlusLocals = checkCells(aryOfGandB,(i,j),k) #Finished checking this far
                    plus1 = 1
                    while len(temparyOfPlusLocals) != 0:
                        plus1+=len(temparyOfPlusLocals)
                        k+=1
                        #Check for distance from walls here
                        if i-k > 0 and i+k < n and j-k > 0 and j+k < m:
                            #checking overlap here
                            temparyOfPlusLocals = checkCells(aryOfGandB,(i,j),k)
                            temp = len(temparyOfPlusLocals)
                            for l in range(temp):
                                if temparyOfPlusLocals[l] in aryOfPlusLocals:
                                    break
                            if l == temp:
                                aryOfPlusLocals+=temparyOfPlusLocals
                        else:
                            break
                    if plus1 != 1:
                        aryOfPlusLocals.append((i,j))
                        if pluses[0] > pluses[1]:
                            pluses[1] = plus1
                        else: pluses[0] = plus1
                else: checker = True
            else:
                checker = False
    #Handling output
    if pluses[0] < 5 or pluses[1] <5:
        if pluses[0] > pluses[1]: print(pluses[0])
        else: print(pluses[1])
    else:
        print(pluses[0]*pluses[1])

#Read in array and call middlelayer method
aryOfGandB = []
for w in range(n):
    s = input()
    aryOfGandB.append(s)


middleLayerIterator(aryOfGandB,n,m)
