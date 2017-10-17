'''
Author: Fionn Mcguire
Date: 17-10-2017
Description: Translate numerical time into textual
'''

h = int(input().strip())
m = int(input().strip())
hours = ["one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve"]
minutes = hours+["thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty","twenty one","twenty two", "twenty three","twenty four","twenty five","twenty six", "twenty seven","twenty eight","half"]

h-=1
minstr = "minutes"
if m == 0:
    minstr = "minute"

if m == 0:
    message = hours[h]+" o' clock"
elif m == 30:
    message = minutes[m]+" "+minstr+" past "+hours[h]
elif m > 30:
    message = minutes[59-m]+" "+minstr+" to "+hours[h+1]
else:
    message = minutes[m]+" "+minstr+" past "+hours[h]
print(message)
