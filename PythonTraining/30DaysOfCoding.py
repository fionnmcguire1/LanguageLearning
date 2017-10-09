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

'''Day 2'''
#Intro to arithmetic operations
def get_total_cost_of_meal():
    # original meal price
    meal_cost = float(input())
    # tip percentage
    tip_percent = int(input())
    # tax percentage
    tax_percent = int(input())

    # Write your calculation code here
    tip = (meal_cost/100)*tip_percent# calculate tip
    tax = (meal_cost/100)*tax_percent# caclulate tax

    # cast the result of the rounding operation to an int and save it as total_cost
    total_cost = int(round(meal_cost+tip+tax))

    return str(total_cost)

# Print your result
print("The total meal cost is " + get_total_cost_of_meal() + " dollars.")

'''Day 3'''
#Intro to if statements
N = int(input().strip())
if (N%2 == 1) or (N%2 == 0 and N in range(6,21)):
    print("Weird")
elif N%2 == 0 and (N in range(2,5) or N > 20):
    print("Not Weird")


'''Day 4'''
class Person:
    def __init__(self,initialAge):
        # Add some more code to run some checks on initialAge
        self.age = initialAge

    def amIOld(self):
        if self.age < 0:
            self.age = 0
            print("Age is not valid, setting age to 0.")
        if self.age < 13:
            print("You are young.")
        elif self.age in range(13,18):
            print("You are a teenager.")
        else:
            print("You are old.")
        # Do some computations in here and print out the correct statement to the console
    def yearPasses(self):
        self.age+=1
        # Increment the age of the person in here

'''Day 5'''
#Dealing with loops
n = int(input().strip())
for i in range(1,11):
    print ("{0} x {1} = {2}".format(str(n),str(i),str(n*i)))

'''Day 6'''
n = int(input())
for i in range(n):
    str1 = ""
    str2 = ""
    strInQuestion = str(input())
    for j in range(len(strInQuestion)):
        if j%2==0:
            str2+= strInQuestion[j]
        else:
            str1+= strInQuestion[j]
    str2+= " "+str1
    print(str2)

'''Day 7'''
n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
n = n-1
str1 = ""
while n > -1:
    str1+= str(arr[n])+" "
    n-=1
print(str1)

'''Day 8'''
#Dictionaries
size = int(input())
phonebook = {}
for i in range(size):
    contact = input().split(' ')
    phonebook[contact[0]] = contact[1]

for i in range(size):
    query = str(input())
    if str(query) in phonebook.keys():
        print("{}={}".format(query,phonebook[query]))
    else:
        print("Not found")

'''Day 9'''
#Recursion
def factorial(n):
    # Complete this function
    result = 1
    i = n
    while i > 0:
        result = i*result
        i-=1
    return result
