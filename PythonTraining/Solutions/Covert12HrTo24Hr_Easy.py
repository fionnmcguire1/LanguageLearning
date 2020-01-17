'''
Author: Fionn Mcguire
Date: 21-09-2017
Description: Covert 12 hour time format to 24 hour  
'''

import sys

def timeConversion(s):
    # Complete this function
    if s[-2:] == "PM":
        newHour = (int(s[0:2])+12)%24
        if newHour != 0:
            s = str(newHour)+s[2:len(s)]
        s = s[0:-2]
    else:
        newHour = (int(s[0:2])+12)%24
        if newHour == 0:
            newHour = "00"
            s = str(newHour)+s[2:len(s)]
        s = s[0:-2]
    return(s)
        

s = input().strip()
result = timeConversion(s)
print(result)
