#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def isBalanced(s):
    bracket_list = []
    if s[0] in [']','}',')']: return "NO"
    if len(s)>0 and s[-1] in ['[','{','(']: return "NO"
    for bracket in s:
        if bracket in ['[','{','(']: bracket_list.append(bracket)
        else:
            try: checkingValue = bracket_list.pop()
            except: return "NO"
            if bracket == ']' and checkingValue =='[': pass
            elif bracket == '}' and checkingValue =='{':pass
            elif bracket == ')' and checkingValue =='(': pass
            else: return "NO"
    return "YES"
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
