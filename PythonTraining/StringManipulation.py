'''
Author: Fionn Mcguire
Date: 10-10-2017
Description String manipulation

'''

'''Print a Welcome Mat in givne dimmentions'''
N, M = map(int,input().split()) # More than 6 lines of code will result in 0 score. Blank lines are not counted.
for i in range(1,N,2):
    print ("{}{}{}".format("-"*(M//2-(i+(i//2))),".|."*((i)),"-"*(M//2-(i+(i//2)))))
print ("{}WELCOME{}".format("-"*N,"-"*N))
for i in range(N-2,-1,-2):
    print ("{}{}{}".format("-"*(M//2-(i+(i//2))),".|."*((i)),"-"*(M//2-(i+(i//2)))))


'''Swap cases in string'''
def swap_case(s):
    str1 = ""
    for i in s:
        if i.isupper():
            str1+=i.lower()
        else:
            str1+=i.upper()
    return str1

'''Split and join a string'''
def split_and_join(line):
    return "-".join(line.split(' '))


'''Find number of occurances of substring in string'''
def count_substring(string, sub_string):
    length = len(sub_string)
    counter = 0
    for index,i in enumerate(string):
        if string[index:index+length] == sub_string:
            counter+=1
    return counter
