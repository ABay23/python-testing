
# * This is a commun intervew exercise
# * Find a value from list 1 in list 2.
# * First Approach is On**2 with 2 nested for loops

# def item_in_common(list1, list2):
#     for i in list1:
#         for j in list2:
#             if i == j:
#                 return True
#     return False


list1 = [1, 3, 5]
list2 = [2, 4, 6]

print(item_in_common(list1, list2))

# * Second Approach is On with 1 nested for loop to populate the dictionary and a second one (not nested) to compare


def item_in_common(list1, list2):
    my_dict = {}
    for i in list1:
        my_dict[i] = True
    for j in list2:
        if j in my_dict:
            print(my_dict)
            return True
    return False


list1 = [1, 3, 5]
list2 = [2, 4, 5]


print(item_in_common(list1, list2))
