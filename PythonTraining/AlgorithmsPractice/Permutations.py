def permuteRemainingString(string_val="",permutation_array=[],active_permutation=""):
    if len(active_permutation) == len(string_val): permutation_array.append(active_permutation)
    else:
        for letter in string_val:
            if letter not in active_permutation:
                permutation_array = permuteRemainingString(string_val,permutation_array,active_permutation+letter)

    return permutation_array

print(len(permuteRemainingString("BOATS")))
