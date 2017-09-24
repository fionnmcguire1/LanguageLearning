"""
Author: Fionn Mcguire
Date: 23-09-2017
Description:


"""

def deletion_distance(str1, str2):
    deletionDistance = 0
    if len(str1) < len(str2):
        str3,str4 = str1,str2
    else:
        str4,str3 = str1,str2
    for index, i in enumerate(str3):
        if str4.find(i) == -1:
            del str3[index]
            del str4[index]
            deletionDistance+=2
    for index, i in enumerate(str4):
        if str3.find(i) == -1:
            del str3[index]
            del str4[index]
            deletionDistance+=2
            
    if len(str3) < len(str4):
        str1,str2 = str3,str4
    else:
        str2,str1 = str3,str4
    iterator = 0
    while iterator < len(str1):
        if str1[iterator] != str2[iterator]:
            del str2[iterator]
            deletionDistance+=1
            iterator-=1
        iterator+=1
    print(str1)
    print(str2)
    if str1 == str2:
        return(deletionDistance)
    else:
        return(0)



str1,str2 = "",""
print(deletion_distance(str1, str2))
str1,str2 = "hello","helo"
print(deletion_distance(str1, str2))
str1,str2 = "hi","hey"
print(deletion_distance(str1, str2))
str1,str2 = "pallindrome","paldrome"
print(deletion_distance(str1, str2))
str1,str2 = "michael","mike"
print(deletion_distance(str1, str2))
str1,str2 = "dan","daniel"
print(deletion_distance(str1, str2))
str1,str2 = "daniel","danielle"
print(deletion_distance(str1, str2))
str1,str2 = "chap","child"
print(deletion_distance(str1, str2))
str1,str2 = "shirt","cap"
print(deletion_distance(str1, str2))
str1,str2 = "holy","watery"
print(deletion_distance(str1, str2))
