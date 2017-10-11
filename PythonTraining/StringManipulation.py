'''
Author: Fionn Mcguire
Date: 10-10-2017
Description String manipulation

'''

'''Print a Welcome Mat in givne dimmentions'''
N, M = 7,21
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
s = "String"
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

thickness = 5 #This must be an odd number
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


'''
Find duplicate if there are characters in string
'''

def DuplicateChar(s):
    try:
        s = str(s)
    except ValueError:
        return "Data entered in method \"DucplicateChar\" was inconsistant with the data type allowed\n"+ValueError
    length = len(s)
    if length > 0:
        s =''.join(sorted(s))
        for i in range(length-1):
            if s[i] == s[i+1]:
                return True
    return False


string = "Hello"
string2 = "Mcguire"
string3 = 456789

#print(DuplicateChar(string))
#print(DuplicateChar(string2))
#print(DuplicateChar(string3))

def checkPermutation(s1,s2):
    try:
        s1 = str(s1)
        s2 = str(s2)
    except ValueError:
        return "Data entered in method \"DucplicateChar\" was inconsistant with the data type allowed\n"+ValueError

    if len(s1) == len(s2):
        if s1 == s2 or sorted(s1) == sorted(s2):
            return True
    return False

string = "Hello"
string2 = "Mcguire"
string3 = 456789
string4 = 547896

#print(checkPermutation(string,string2))
#print(checkPermutation(string3,string4))
#print(checkPermutation(string,string4))
#print(checkPermutation(string3,string2))

'''Check if string is a permustation of a pallindrome'''
def CheckPallinPerm(s):
    #import string
    #s = s.translate(None, string.punctuation)
    str1 = s
    str1 = str1.replace(" ","")
    str1 = str1.lower()

    length = len(str1)
    checker = 1
    if length > 0:
        if length%2 == 1:
            checker = 0
        str1 = sorted(str1)
        #print(str1)
        checker2 = False
        for i in range(0,length-1,2):
            if checker2 == True:
                i-=1
                checker2 = False
            if str1[i] == str1[i+1]:
                pass
            else:
                checker+=1
                checker2 = True
                #print("{} {}".format(str1[i],str1[i+1]))
                if checker > 1:
                    return False

    return True


string = "Hello"
string2 = "BOB"
string3 = "Amy must I jujitsu my ma"
string4 = "Aibohphobia"
#print(CheckPallinPerm(string))
#print(CheckPallinPerm(string2))
#print(CheckPallinPerm(string3))
#print(CheckPallinPerm(string4))
#Expected output F,T,T,T

'''
Given two strings see if they're one character away from being equal (insert,delete,replace)
'''

def almost_there(s1,s2):
    len1,len2 = len(s1),len(s2)
    s1,s2 = s1.lower(),s2.lower()
    checker = 0
    if len1 == len2 or (len1-len2) == 1 or (len2-len1) == 1:
        if len1 > len2: n = len2
        else: n = len1
        for i in range(n):
            j = i
            if checker>=1:
                if len1 == len2: pass
                elif len1 > len2: i+=1
                else: j+=1

            if s1[i] != s2[j]:
                checker+=1
                if checker > 1: return False
        return True
    else: return False

s1,s2 = "pale", "ple"
#print(almost_there(s1,s2))
s1,s2 = "pale", "pales"
#print(almost_there(s1,s2))
s1,s2 = "pale", "bale"
#print(almost_there(s1,s2))
s1,s2 = "ple", "plea"
#print(almost_there(s1,s2))
s1,s2 = "sarah", "John"
#print(almost_there(s1,s2))

'''Compress a string by repeating characters'''
def Compressed(s):
    n = len(s)
    counter = 1
    compressed = ""
    for i in range(n-1):
        if s[i] == s[i+1]:
            counter+=1
        else:
            compressed+=s[i]+str(counter)
            counter = 1
    if n > len(compressed):
        return compressed
    else:
        return s
'''
s = "aaaabbbbbcccdeeeffg"
print(s)
print(Compressed(s))
s = "aaabbbcccdeeeffg"
print(s)
print(Compressed(s))
s = "abbbbbeeffg"
print(s)
print(Compressed(s))
s = "fionnmcguire"
print(s)
print(Compressed(s))
s = "ffffiiooonnnnnmmcccgguuiirrre"
print(s)
print(Compressed(s))'''
