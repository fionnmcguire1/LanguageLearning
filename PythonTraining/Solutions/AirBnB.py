'''
Input: String
AirBnB simulated 30min interview:
    1. Reverse a string
    2. Find missing element in list
    3. Find all combinations of a string
Author: Fionn Mcguire
Date: 29-01-2020
'''



def rev_string(input_string):
    reversed_string = ""
    index = -1
    length_of_string = (len(input_string)+1)*-1

    while index != length_of_string:
        reversed_string+=input_string[index]
        index-=1
    #return sorted(input_string,reverse=True)
    return reversed_string

print(rev_string("Hello"))



def find_missing(first_array,second_array):
    tracking_number_hash = dict()
    missing_numbers = []

    for number in second_array:
        if number in tracking_number_hash.keys():
            tracking_number_hash[number]+=1
        else:
            tracking_number_hash[number]=1

    for number in first_array:
        if number in tracking_number_hash.keys():
            if tracking_number_hash[number] == 0: missing_numbers.append(number)
            else: tracking_number_hash[number] -=1
        else: missing_numbers.append(number)

    return missing_numbers

print(find_missing([1,2,3,4,4,5,5,5,5,5,5,6],[1,2,3]))


#Another way of doing this problem is with sets
def find_missing_sets(first_array,second_array):
    missing_items = set(first_array) - set(second_array)
    assert(len(missing_items) == 1)
    return list(missing_items)[0]


print(find_missing_sets([1,2,3,4],[1,2,3]))


input_str = '123'
def print_each_letter(combinations,current_combo,input_str):
    index = len(current_combo)
    for letter in range(index,len(input_str)):
        if len(current_combo)+1 == len(input_str): combinations.append(current_combo+input_str[letter])
        else: combinations = print_each_letter(combinations,current_combo+input_str[letter],input_str)
    return combinations
combinations = print_each_letter([],"",input_str)
print(combinations)
print(len(combinations))
