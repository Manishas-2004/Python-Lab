# 4. Write a Python program to split a given list into two parts where the length of the first part of the list is given. 

#Original list: [1, 1, 2, 3, 4, 4, 5, 1] Length of the first part of the list: 3 Splitted the said list into two parts: ([1, 1, 2], [3, 4, 4, 5, 1])

def split_list(lst, length):
    return lst[:length], lst[length:]
original_list = [1, 1, 2, 3, 4, 4, 5, 1]
length_of_first = 3
print(split_list(original_list, length_of_first))  
