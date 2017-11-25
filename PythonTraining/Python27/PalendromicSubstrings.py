'''
Author: Fionn Mcguire
Date: 25-11-2017
Description: Given a string, your task is to count how many palindromic substrings in this string.
The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.
'''

'''
Requirements:
    Traverse through string
    Add length of string to answer
    Get substring
    Test if a substring is a pallindrome

    create hash function to store a list of indexs of letters
    any sublist with more than one entry test for pallindome

'''
InputString = raw_input("Please enter a string: ")

dictOfIndexes = {}
ListOfOrganisedChars = []
def hash_function(ListOfOrganisedChars, dictOfIndexes,char,index):
    if char in dictOfIndexes:
        ListOfOrganisedChars[dictOfIndexes[char]].append(index)
    else:
        dictOfIndexes[char] = len(ListOfOrganisedChars)
        ListOfOrganisedChars.append([index])
    return dictOfIndexes,ListOfOrganisedChars
for index,value in enumerate(InputString):
    dictOfIndexes,ListOfOrganisedChars = hash_function(ListOfOrganisedChars, dictOfIndexes,value,index)

totalPsubs = len(InputString)
Length = len(ListOfOrganisedChars)
for i in xrange(Length):
    if len(ListOfOrganisedChars[i]) > 1:
        for j in xrange(len(ListOfOrganisedChars[i])-1):
                k = 1
                while k+j < len(ListOfOrganisedChars[i]):
                    str1 = InputString[ListOfOrganisedChars[i][j]:(ListOfOrganisedChars[i][j+k]+1)]
                    if str1 == str1[::-1]:
                        totalPsubs+=1
                    k+=1

print "Total Palindromic Substrings: ",; print totalPsubs

#print(ListOfOrganisedChars)

