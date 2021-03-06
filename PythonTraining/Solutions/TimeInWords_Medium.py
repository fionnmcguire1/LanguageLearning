'''
Author: Fionn Mcguire
Date: 17-10-2017
Description: Translate numerical time into textual
'''

def timeInWords(h,m):
    hours = ["one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve"]
    minutes = hours+["thirteen","fourteen","quarter","sixteen","seventeen","eighteen","nineteen","twenty","twenty one","twenty two", "twenty three","twenty four","twenty five","twenty six", "twenty seven","twenty eight","twenty nine","half"]
    m-=1
    h-=1
    minstr = " minutes"
    direction = " past "
    if m == 0:
        minstr = " minute"
    elif m == 14 or m == 44:
        minstr = ""
    if m > 29:
        direction = " to "


    if m == -1:
        message = hours[h]+" o' clock"
    elif m == 29:
        message = minutes[m]+direction+hours[h]
    elif m > 29:
        message = minutes[58-m]+minstr+direction+hours[h+1]
    else:
        message = minutes[m]+minstr+direction+hours[h]
    print(message)

timeInWords(5,45)
