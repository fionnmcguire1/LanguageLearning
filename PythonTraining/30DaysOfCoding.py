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

'''Day 0.5 (Accidentally did one of the other tasks)'''
#Print the sum of imputted array where the input is 2 lines the
#First input is N (size of the array)
#Second line is the array
n = int(input())
array = list(map(int, input().strip().split(' ')))

result = 0
for index,i in enumerate(array):
    result+=int(array[index])
print(result)

'''Day 1'''
i = 15
d = 4.0
s = " there buddy"

# Read and save an integer, double, and String to your variables.
integerinput = int(input())
floatinput = float(input())
str1 = str(input())
# Print the sum of both integer variables on a new line.
print(integerinput+i)
# Print the sum of the double variables on a new line.
print(floatinput+d)
# Concatenate and print the String variables on a new line
str2 = s+str1
print(str2)
