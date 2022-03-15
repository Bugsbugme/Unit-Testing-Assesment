# count_characters function

# author: A. N. Other # date: 15 June 2017

# Purpose:
# A function that returns the number of upper and lowercase letters
# from a parameter string.
# The function returns a list of 3 numbers:
# [ <Upper case letters>, <Lower case letters>, <Other characters> ]

def count_characters(word):
    upper_case, lower_case, other_characters = 0, 0, 0

    for key, value in enumerate(word): 
        if value.isupper():
            upper_case += 1
        elif value.islower():
            lower_case += 1
        else:
            other_characters += 1

    return [upper_case, lower_case, other_characters]