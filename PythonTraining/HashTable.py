'''
Author: Fionn Mcguire
Date: 03-10-2017
Description: Implement a hash table

'''


'''
Hash tables have a hash function and a table. The hash function governs where
to input the value in the table based on the key. The hash function outputs an index of the table
where the value will be stored. This must be consistant for the same keys. Collisions occur
when two values are stored in the same index. I.e when two values provide the same key.
eg if the key is the first char of a string and you want to store. The hash "ant" and "apple", their keys would
be "a". The hash function takes in "a" and outputs 0 sending the values to table[0].


Methods for resolving collisions:
Linear probing: If a key hashes to a previously stored index then the value is sent to
the next available slot in the table. Once a collision occurs you've significantly increased chances of
collisions occuring in the same area. This is called clustering.

Seperate chaining: This is where the table is an array of pointers to linked lists.
When a collision occurs, the value can be stored as the head of the correct linked list.

Note: Untilize as much info on the key as possible. This increases the size of the table and reduces the
chance of collisions making insert, delete and lookup much faster.
'''

table = [[] for a in range(10)]
def hashingFunction(num):
    return num%10
def insert(table,key,value):
    table[hashingFunction(key)].append(value)

insert(table,115,"Hey")
insert(table,115,"hi")
insert(table,7,"hello")
insert(table,8943,"yellow")
insert(table,33,"ahoy")
insert(table,99,"Alright")
print(table)



    
