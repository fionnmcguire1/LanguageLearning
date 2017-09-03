'''
Author: Fionn Mcguire
Lynda.com python training
'''


print("Hello World")
a,b = "Fionn","Python 3"


#Note that when using format, if you're printing the variables in order, you can use
#{}, if you want to reuse the variables and/or print them out of order you can use {0} or {1}

print("Hello {0}, you're programming in {1}".format(a,b))
print("{1} is the language you're programming in {0}, isn't {1} good?".format(a,b))

x,y = 6,7

if x < y:
    print("{} is less than {}".format(x,y))
else:
    print("{} is less than {}".format(y,x))

#You can also place a simple if inside the print statement
print("Nice" if x < y else "One")

#Demonstrating a while loop fibonacci series 
a,b,c = 1,1,5000
while a < c:
    print(a)
    d = a+b
    b = a
    a = d

#Demonstrting for loop
for x in range (0 , 10):
    print("Index {}".format(x))

def isPrime(x):
    if x == 0 or x == 1:
        print("{} is Prime (Debatable)".format(x))
    else:
        i = 2
        checker = True
        while i < x:
            if x%i == 0:
                checker = False
                exit
            i+=1
        if checker == True:
            print("{} is Prime".format(x))

def efficientPrime(start,end):
    #Function to list all of the primes within a certain range
    #This improves speed
    #I'm using a string rather than an array as a string can be printed
    #easily, while an array must iterate through, printing each element resulting in the same inefficiency

    x = start
    primes_str = ''
    while x < end:
        if x == 0 or x == 1:
            primes_str+= "{} is Prime\n".format(x)
        else:
            i = 2
            checker = True
            while i < x:
                if x%i == 0:
                    checker = False
                    exit
                i+=1
            if checker == True:
                primes_str+= "{} is Prime\n".format(x)
        x+=1
    print(primes_str)
            
    
'''
i = 0
while i < 100:
    isPrime(i)
    i+=1
'''

efficientPrime(1,100)

#Demonstrating basic class with methods and uses
class fibonacci():
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def series(self):
        while(True):
            yield(self.b)
            self.a, self.b = self.b, self.a + self.b
            


f = fibonacci(0,1)
for r in f.series():
    if r > 100: break
    print(r)

#Demonstrating inheritance and polymorphism
class schedule:
    def printSchedule(self):
        print(self.schedule["daily"])

class oap(schedule):
    schedule = dict(
        daily = "9am: Breakfast\n 11am Golf\n 4pm Tea\n 8pm Supper\n 9:30pm Bed",
        events = "Retirement party 11th August 2018"
        )

class student(schedule):
    schedule = dict(
        daily = "7am: Breakfast\n 9am School\n 4pm Homework\n 6pm Dinner\n 7pm Football\n 11:30pm Bed"
        )

class child(schedule):
    schedule = dict(
        daily = "7am: Breakfast\n 9am Nanny comes over\n 4pm Tea\n 8pm Supper\n 7:30pm Bed"
        )

Arther = oap()
Billy = student()
Tommy = child()

print("Arther's Schedule")
Arther.printSchedule()
print("Billy's Schedule")
Billy.printSchedule()
print("Tommy's Schedule")
Tommy.printSchedule()

try:
    file = open("file.txt")
    for line in file.readlines():
        print(line)
except IOError as e:
    print("There was an error!\n {}".format(e))


    

    
