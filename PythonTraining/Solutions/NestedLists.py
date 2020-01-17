#Passed 8 out of 10 test cases
#
# if __name__ == '__main__':
#     scoreList = []
#     grades = []
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())
#
#
#         scoreList.append(score)
#         grades.append([name,score])
#
#     scoreList = sorted(scoreList)
#     secondLowest = scoreList[1]
#
#     nameList = []
#     for grade in grades:
#         if grade[1] == secondLowest:
#             nameList.append(grade[0])
#
#
#     for i in sorted(nameList):
#         print(i)




if __name__ == '__main__':

    #Organising the data into hashmaps
    physicsHashMap = dict()
    for _ in range(int(input())):
        name = input()
        score = float(input())

        if score in physicsHashMap.keys(): physicsHashMap[score].append(name)
        else: physicsHashMap[score] = [name]

    scoreToBePrinted = sorted(physicsHashMap.keys())[1]

    for printName in physicsHashMap[scoreToBePrinted]:
        print(printName)
