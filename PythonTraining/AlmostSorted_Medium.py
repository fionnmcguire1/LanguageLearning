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
i,j = 0,0
checker = False
operation = "swap"
while i < n:
    j = i+1
    while j < n:
        listToBeSorted[i],listToBeSorted[j] = listToBeSorted[j],listToBeSorted[i]
        if sortedList == listToBeSorted:
            print("yes")
            print("swap {0} {1}".format(i+1,j+1))
            checker = True
            i = n+1
            break 
        else:
            listToBeSorted[i],listToBeSorted[j] = listToBeSorted[j],listToBeSorted[i]
            listToBeSorted[i:j] = listToBeSorted[i:j][::-1]
            if sortedList == listToBeSorted:
                print("yes")
                print("reverse {0} {1}".format(i+1,j))
                checker = True
                i=n+1
                break
            else:
                listToBeSorted[i:j] = listToBeSorted[i:j][::-1]
        
        
        j+=1
    i+=1
    
if checker == False:
    print("no")
