#!/usr/bin/python3
replace_in_list = __import__('2-replace_in_list').replace_in_list

list = [1, 2, 3]
idx = 3
new_element = 4
new_list = replace_in_list(list, idx, new_element)

print(new_list)
print(list)
