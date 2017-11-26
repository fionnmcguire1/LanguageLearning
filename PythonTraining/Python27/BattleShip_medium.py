'''
Author: Fionn Mcguire
Date: 26-11-2017
Description:
Given an 2D board, count how many battleships are in it. The battleships are represented with 'X's, empty slots are represented with '.'s. You may assume the following rules:

    You receive a valid board, made of only battleships or empty slots.
    Battleships can only be placed horizontally or vertically. In other words, they can only be made of the shape 1xN (1 row, N columns) or Nx1 (N rows, 1 column), where N can be of any size.
    At least one horizontal or vertical cell separates between two battleships - there are no adjacent battleships.
'''


class Solution(object):
        def countBattleships(self, board):
                    """
                    :type board: List[List[str]]
                    :rtype: int
                    """
                    numBattleships = 0
                    for line in xrange(len(board)):
                        for element in xrange(len(board[line])):
                            if board[line][element] == 'X':
                                if line != 0:
                                    if board[line-1][element] != 'X':
                                        if element != 0:
                                            if board[line][element-1] != 'X':
                                                numBattleships+=1  
                                        else:
                                            numBattleships+=1  
                                else: 
                                    if element != 0:
                                        if board[line][element-1] != 'X':
                                            numBattleships+=1
                                    else:
                                        numBattleships+=1
            return numBattleships

