from collections import defaultdict

#Find the first duplicate in a list
def FindDuplicate(input_arr):
    if len(input_arr) >1:
        comparisson_hash = defaultdict(int)
        for num in input_arr:
            comparisson_hash[num]+=1
            if comparisson_hash[num] == 2:
                return num
    return -1




print("Find First Duplicate: ",FindDuplicate([1,1,2,3,4,5,6,7,7]))


#First solution for find the longest common string in two strings
def findLongestCommonString(first_list,second_list):
    largest_sub_string = ""
    first_len = len(first_list)
    second_len = len(second_list)
    for start_index in range(first_len):
        for moving_pointer in range(start_index,first_len):
            comparable_str = first_list[start_index:moving_pointer]
            if comparable_str in second_list and len(comparable_str) >= len(largest_sub_string):
                largest_sub_string = comparable_str
    return largest_sub_string

print("Find Longest Common String: ",findLongestCommonString("GEEKSFORGEEKS","GEEKSQUIZ"))
