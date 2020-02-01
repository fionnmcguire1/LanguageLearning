#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    nList = [0]*n
    max_num = 0
    #fuck sake make it into a hashmap
    for l in queries:
        for index in range(l[0]-1,l[1]):
            nList[index]+=l[2]
            if nList[index] > max_num: max_num= nList[index]
    return max_num

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
