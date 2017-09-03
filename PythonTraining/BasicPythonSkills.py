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
