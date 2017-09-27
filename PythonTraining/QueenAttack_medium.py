'''
Author: Fionn Mcguire
Date: 25-09-2017
Description:
    Count the number of moves the queen can make given the position of obstacles on a set size board
'''
import sys

#Taking in inputs
#n,k = dimension size and number of obstacles
n,k = input().strip().split(' ')
n,k = [int(n),int(k)]

#Position of queen
rQueen,cQueen = input().strip().split(' ')
rQueen,cQueen = [int(rQueen)-1, int(cQueen)-1]

#Building the chess board
chessBoard = [[0 for i in range(n)] for j in range(n)]
chessBoard[rQueen][cQueen] = 3
#Taking in the obstacles(other pieces)
for a in range(k):
    rObstacle,cObstacle = input().strip().split(' ')
    rObstacle,cObstacle = [int(rObstacle),int(cObstacle)]
    chessBoard[rObstacle-1][cObstacle-1] = 2
i,j = rQueen,cQueen
print(chessBoard)
#Count how many possible moves they can make
moves = 0
#There are 8 possible directions to go from any point
#Concidering bottom/top left diagonal ect
Direction = 0
'''
Go through each possible direction
'''
while True:

    if Direction == 0:
        i-=1
        if i > -1:
            if chessBoard[i][cQueen] == 0:
                moves+=1
            else:
                i = rQueen
                Direction+=1                
        else:
                i = rQueen
                Direction+=1  
                
    elif Direction == 1:
        i+=1
        if i < n:
            if chessBoard[i][cQueen] == 0:
                moves+=1
            else:
                i = rQueen
                Direction+=1                
        else:
                i = rQueen
                Direction+=1  
    elif Direction == 2:
        j+=1
        if j > -1 and j < n:
            if chessBoard[rQueen][j] == 0:
                moves+=1
            else:
                j = cQueen
                Direction+=1  
        else:
                j = cQueen
                Direction+=1  
    elif Direction == 3:
        j-=1
        if j < n:
            if chessBoard[rQueen][j] == 0:
                moves+=1
            else:
                j = cQueen
                Direction+=1  
        else:
                j = cQueen
                Direction+=1  
                
    elif Direction == 4:
        j-=1
        i-=1
        if j > -1 and i > -1:
            if chessBoard[i][j] == 0:
                moves+=1
            else:
                j = cQueen
                i = rQueen
                Direction+=1  
        else:
                j = cQueen
                i = rQueen
                Direction+=1  
    elif Direction == 5:
        j+=1
        i+=1
        if j < n and i < n:
            if chessBoard[i][j] == 0:
                moves+=1
            else:
                j = cQueen
                i = rQueen
                Direction+=1  
        else:
                j = cQueen
                i = rQueen
                Direction+=1  
    elif Direction == 6:
        j-=1
        i+=1
        if j > -1 and i < n:
            if chessBoard[i][j] == 0:
                moves+=1
            else:
                j = cQueen
                i = rQueen
                Direction+=1  
        else:
                j = cQueen
                i = rQueen
                Direction+=1  
    elif Direction == 7:
        j+=1
        i-=1
        if j < n and i > -1:
            if chessBoard[i][j] == 0:
                moves+=1
            else:
                j = cQueen
                i = rQueen
                Direction+=1  
        else:
                j = cQueen
                i = rQueen
                Direction+=1  
    else:
        print(moves)
        break
            
