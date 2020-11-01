
list_of_elements = [1,2,3,4,5,6,7,2,1,2,3,4,3,2,1,1,10]
set_of_list = set(list_of_elements)

list_of_other_elements = [1,2,3,4,68]
set_of_second_list = set(list_of_other_elements)

demo_minus = set_of_list - set_of_second_list
demo_minus2 = set_of_second_list - set_of_list
demo_plus = set_of_list | set_of_second_list
demo_both = set_of_list &set_of_second_list
demo_or = set_of_list ^set_of_second_list


print(list_of_elements)
print(set_of_list)

print(demo_minus)
print(demo_minus2)
print(demo_plus)
print(demo_both)


set1 = set([1,2,3,4,5,6,7,8,9])
set2 = set([6,7,8,9,10,11,12,13,14,15])
set3 = set([8,9,15,16,17,18,19,1,2])

print(set1.intersection(set2))
print(set1.intersection(set2,set3))
print(set1.intersection(set2,set3))
print(set1.difference(set2,set3))
print(set1.symmetric_difference(set2))
