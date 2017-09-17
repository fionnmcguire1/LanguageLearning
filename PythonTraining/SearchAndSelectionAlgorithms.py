'''
Author: Fionn Mcguire
Date: 16-09-2017
Description:
    Search and selection algorithms
'''

#unordered list
sample_dataset = [0,1,2,3,6,7,5,4,56,765,32,45,98,-22,4,5,-456,1,8,88,-11,-0]

#ordered list
sample_dataset_ordered = [0,1,4,7,9,44,66,77,87,98,]


#find min
def findmin (sample_dataset):
    i = 0
    while i < len(sample_dataset):
        if i == 0:
            temp = sample_dataset[i]
        else:
            if sample_dataset[i] < temp:
                temp = sample_dataset[i]
        i+=1
    return temp

min_num = findmin(sample_dataset)
print(min_num)
min_num = findmin(sample_dataset_ordered)
print(min_num)
print(max(sample_dataset))

#sorting_algorithms







