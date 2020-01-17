#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):

    magazineDict = dict()
    for i in range(len(magazine)):
        if magazine[i] in magazineDict.keys(): magazineDict[magazine[i]].append(i)
        else: magazineDict[magazine[i]] = [i]

    for word in note:
        if word in magazineDict.keys():
            magazineDict[word].pop()
            if len(magazineDict[word]) == 0: del magazineDict[word]
        else:
            print("No")
            return
    print("Yes")


if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
