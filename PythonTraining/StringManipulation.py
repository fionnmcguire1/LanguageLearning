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

'''Figure out the properties of a string'''
s = input()
alphanum,alpha,digets,lower,upper = False,False,False,False,False
for i in s:
    if i.isalnum():
        alphanum = True
        if i.isalpha():
            alpha = True
            if i.islower():
                lower = True
            elif i.isupper():
                upper = True
        if i.isdigit() :
            digets = True

print(alphanum)
print(alpha)
print(digets)
print(lower)
print(upper)

'''Create Hackerrank Logo with string formatting alignment'''

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))