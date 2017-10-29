'''
Author: Fionn Mcguire
Date: 26-09-2017

Description:
    Working with tuples and dictionaries
'''
#These are useful for throwing together a load of different data types
#Issue is you can't change the value of a tuple object

#Tuples are generated faster and is iterated through faster
tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5 )
tup3 = "a", "b", "c", "d"
tup4 = (5)
print(tup4)


#Dictionaries
mydict = {"Fionn": 23, "Richie": 24, "Sarah": 24, "Sarabeth": 28, "Katie": 33}

print(mydict)
#print element
#print(mydict["Fionn"])
sortedKeys = sorted(mydict.keys())
sortedValues = sorted(mydict.values())
#del mydict["Richie"]
#Delete from dictionary
#print(mydict)

#Check if key in dictionary
'''if "James" in mydict:
    #print(True)
elif "James" not in mydict:
    #print(False)
'''
#iterate through dictionary
'''for i,j in mydict.items():
    #print("{} with value {}".format(i,j))
'''
#Another way to iterate through mydict
'''for i in mydict:
    print(i)
    print(mydict[i])
'''
#Sorted dict: sorts by values and alphabetically in the event of duplicates
def sortDict(mydict):
    secondDict = {}
    for i,j in mydict.items():
        if j not in secondDict:
            secondDict[j] = list()
        secondDict[j].append(i)

    sortedValues = sorted(secondDict.keys())
    sortedValues = sortedValues[::-1]
    ReturnValue = []
    for i in sortedValues:
        if len(secondDict[i]) != 1:
            secondDict[i] = sorted(secondDict[i])
        for j in secondDict[i]:
            ReturnValue.append(j)
    return ReturnValue


print(sortDict(mydict))
