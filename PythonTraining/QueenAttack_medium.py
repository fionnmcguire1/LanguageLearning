'''
Author: Fionn Mcguire
Date: 25-09-2017
Description:
    Count the number of moves the queen can make given the position of obstacles on a set size board
'''

n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
rQueen,cQueen = input().strip().split(' ')
rQueen,cQueen = [int(rQueen),int(cQueen)]
chessBoard = [[0 for i in range(n)] for j in range(n)]
chessBoard[rQueen,cQueen] = 3
for a0 in range(k):
    rObstacle,cObstacle = input().strip().split(' ')
    rObstacle,cObstacle = [int(rObstacle),int(cObstacle)]
    chessBoard[rObstacle,cObstacle] = 2
i,j = rQueen,cQueen
moves = 0
LeftLateral = False
RightLateral = False
TopHorizontal = False
BottomHorizontal = False
LeftTopDiagonal = False
RightTopDiagonal = False
LeftBottomDiagonal = False
RightBottomDiagonal = False
while true:

    if LeftLateral == False:
        i-=1
        if i > -1:
            if chessBoard[i,cQueen] == 0:
                moves+=1
            else:
                i = rQueen
                LeftLateral = True
        else:
                i = rQueen
                LeftLateral = True
    elif RightLateral == False:
        i+=1
        if i < n:
            if chessBoard[i,cQueen] == 0:
                moves+=1
            else:
                i = rQueen
                RightLateral = True
        else:
                i = rQueen
                RightLateral = True
    elif TopHorizontal == False:
        j+=1
        if j > -1:
            if chessBoard[rQueen,j] == 0:
                moves+=1
            else:
                j = cQueen
                TopHorizontal = True
        else:
                j = cQueen
                TopHorizontal = True 
    elif BottomHorizontal == False:
        j-=1
        if j < n:
            if chessBoard[rQueen,j] == 0:
                moves+=1
            else:
                j = cQueen
                BottomHorizontal = True
        else:
                j = cQueen
                BottomHorizontal = True
    elif LeftTopDiagonal == False:
        j-=1
        i-=1
        if j > -1 and i > -1:
            if chessBoard[i,j] == 0:
                moves+=1
            else:
                j = cQueen
                i = rQueen
                LeftTopDiagonal = True
        else:
                j = cQueen
                i = rQueen
                LeftTopDiagonal = True
    elif RightBottomDiagonal == False:
        j+=1
        i+=1
        if j < n and i < n:
            if chessBoard[i,j] == 0:
                moves+=1
            else:
                j = cQueen
                i = rQueen
                RightBottomDiagonal = True
        else:
                j = cQueen
                i = rQueen
                RightBottomDiagonal = True
    elif rightTopDiagonal == False:
        j-=1
        i+=1
        if j > -1 and i < n:
            if chessBoard[i,j] == 0:
                moves+=1
            else:
                j = cQueen
                i = rQueen
                rightTopDiagonal = True
        else:
                j = cQueen
                i = rQueen
                rightTopDiagonal = True
    elif LeftBottomDiagonal == False:
        j+=1
        i-=1
        if j < n and i > -1:
            if chessBoard[i,j] == 0:
                moves+=1
            else:
                j = cQueen
                i = rQueen
                LeftBottomDiagonal = True
        else:
                j = cQueen
                i = rQueen
                LeftBottomDiagonal = True
    else:
        print(moves)
        break
            
    
