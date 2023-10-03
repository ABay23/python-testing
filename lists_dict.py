# Python3 code to demonstrate
# Swap elements in String list
# using replace() + list comprehension

# Initializing list
test_list = ['Gfg', 'is', 'best', 'for', 'Geeks']

# printing original lists
print("The original list is : " + str(test_list))

# Swap elements in String list
# using replace() + list comprehension
res = [sub.replace('G', '-').replace('e', 'G').replace('-', 'e')
       for sub in test_list]

# printing result
print("List after performing character swaps : " + str(res))


# Python3 code to Demonstrate Remove empty List
# from List using list comprehension

# Initializing list
test_list = [5, 6, ['s'], 3, [], [], 9]

# printing original list
print("The original list is : " + str(test_list))

# Remove empty List from List
# using list comprehension
# res = [ele for ele in test_list if ele != []]
res = [x for x in test_list if x != []]

# printing result
print("List after empty list removal : " + str(res))
