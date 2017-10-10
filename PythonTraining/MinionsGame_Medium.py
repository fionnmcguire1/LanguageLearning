'''
Author: Fionn Mcguire
Date: 10-10-2017
Description: Minions game, effectively try and see how many substr there are with vowels and
how many with consonants.

'''

def minion_game(string):
    checker = True
    v = "AEIOU"
    concenant = 0
    vowel = 0
    length = len(string)
    for j in range(length):
        checker = True
        if v.find(string[j]) == -1:
            checker = False
        for i in range(length+1):
            sub = string[j:i]
            if sub == string[j:j+len(sub)]  and len(sub) != 0:
                if checker == False:
                    vowel+=1
                else:
                    concenant+=1
    if vowel < concenant:
        print("Kevin {}".format(str(concenant)))
    elif vowel > concenant:
        print("Stuart {}".format(str(vowel)))
    else:
        print("Draw")
