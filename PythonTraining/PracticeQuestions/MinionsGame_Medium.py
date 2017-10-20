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
        if string[j] not in v:
            checker = False
        for i in range(j,length+1):
            sub = string[j:i]
            if sub == string[j:j+len(sub)] and len(sub) != 0:
                if checker == False:
                    consonant+=1
                else:
                    vowel+=1
    if vowel > concenant:
        print("Stuart {}".format(str(vowel)))
    elif vowel < concenant:
        print("Kevin {}".format(str(consonant)))
    else:
        print("Draw")

'''
Actual solution: NOT MY CODE

def minion_game(s):
    V = frozenset("AEIOU")
    n = len(s)
    ksc = sum(q for c, q in zip(s, range(n, 0, -1)) if c in V)
    ssc = n * (n + 1) // 2 - ksc
    if ksc > ssc:
        print("Kevin {:d}".format(ksc))
    elif ssc > ksc:
        print("Stuart {:d}".format(ssc))
    else:
        print("Draw")
This completed all test cases in record time
'''
