'''
Author: Fionn Mcguire
Date: 25-11-2017
Description: Seek out the differences in python 2.7 and 3
'''

import timeit
a = "My name is "
b = "Fionn"
print "Hello world!",; print "My name is fionn"
print "Hello World! ",; print a,; print "Fionn"



a = 2
b = 3

print float(b)/float(a)

st = ['Fionn', 'Richie', 'Sarabeth']
for index,value in enumerate(st):
    print index,; print value



def test():
    for i in xrange(10000):
        pass

#timeit.timeit(test())

my_generator = (letter for letter in 'abcdefg')

#next(my_generator)
print my_generator.next()



#List comprehension
mylist = [[j for j in xrange(3)] for i in xrange(17)]
print mylist



age = raw_input("Enter your age: ")
print "You are "+str(int(age)//10)+" decades old"








