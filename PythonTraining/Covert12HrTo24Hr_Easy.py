'''
Author: Fionn Mcguire
Date: 21-09-2017
Description: Covert 12 hour time format to 24 hour  
'''




import sys

def timeConversion(s):
    # Complete this function
    if s[-2:] == "PM":
        newHour = int(s[0:2])+12
        s = str(newHour)+s[2:len(s)]
        s = s[0:-2]
    else:
        s = s[0:-2]
    return(s)
        

s = "07:05:45PM"
result = timeConversion(s)
print(result)
