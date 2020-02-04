

def my_generator(big_list):
    for item in big_list:
        yield item



my_big_list = [1,2,3,4,5,6,7,8,9,10,11,12]

my_list_generator = my_generator(my_big_list)

print(my_list_generator.next())
print(my_list_generator.next())
print(my_list_generator.next())
print(my_list_generator.next())

#This starts at element 4 because
#We have already returned the first 4
#Items above
for item in my_list_generator:
    print(item)
