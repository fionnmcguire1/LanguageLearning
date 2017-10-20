'''
Author: Fionn Mcguire
Date: 28-09-2017
Description: Almost sorted, a list is almost sorted. You can
only perform one operation, either a 2 element swap or a subset
reverse. If this finishes off sorting the list then print yes and how
it was done. Otherwise print no

'''
n = int(input())
listToBeSorted = list(map(int, input().strip().split(' ')))
sortedList = sorted(listToBeSorted)
i,j,checker = 0,0,False
for i in range(n):
    j = i+1
    for j in range(j,n):
        listToBeSorted[i],listToBeSorted[j] = listToBeSorted[j],listToBeSorted[i]
        if sortedList == listToBeSorted:
            print("yes")
            print("swap {0} {1}".format(i+1,j+1))
            checker = True           
            break 
        else:
            listToBeSorted[i],listToBeSorted[j] = listToBeSorted[j],listToBeSorted[i]
            if j != i+1 and j != i:
                listToBeSorted[i:j] = listToBeSorted[i:j][::-1]
                if sortedList == listToBeSorted:
                    print("yes")
                    print("reverse {0} {1}".format(i+1,j))
                    checker = True               
                    break
                else:
                    listToBeSorted[i:j] = listToBeSorted[i:j][::-1]        
    if checker == True:
        break  
if checker == False:
    print("no")
