"""
Author: Fionn Mcguire
Date: 23-09-2017
Description:


"""

def deletion_distance(str1, str2):
    cur = list(range(len(str2) + 1))
    prev = [0] * (len(str2) + 1)
    for i in range(len(str1)):
        cur, prev = prev, cur
        cur[0] = i + 1
        for j in range(len(str2)):
            # Substitution is same as two deletions
            sub = 0 if str1[i] == str2[j] else 2
            cur[j+1] = min(prev[j] + sub, cur[j] + 1, prev[j+1] + 1)

    return cur[-1]



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
