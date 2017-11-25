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
for i in xrange(40):
    if i < 5:
        dictOfIndexes,ListOfOrganisedChars = hash_function(ListOfOrganisedChars, dictOfIndexes,'a',i) 
    elif i > 5 and i < 15: 
        dictOfIndexes,ListOfOrganisedChars = hash_function(ListOfOrganisedChars, dictOfIndexes,'b',i)
    elif i > 15 and i < 25:
        dictOfIndexes,ListOfOrganisedChars = hash_function(ListOfOrganisedChars, dictOfIndexes,'c',i)
    else:
        dictOfIndexes,ListOfOrganisedChars = hash_function(ListOfOrganisedChars, dictOfIndexes,'d',i)
print(ListOfOrganisedChars)












