'''
Author: Fionn Mcguire
Date: 09-10-2017
Description: Hackerank-->30 Days of coding

'''

'''Day 0'''
#Read line from stdin
input_string = input()
# Print a string literal saying "Hello, World." to stdout.
print('Hello, World.')
#Output string taken in
print(input_string)

'''Day 1'''
#Print the sum of imputted array where the input is 2 lines the
#First input is N (size of the array)
#Second line is the array
n = int(input())
array = list(map(int, input().strip().split(' ')))

result = 0
for index,i in enumerate(array):
    result+=int(array[index])
print(result)
