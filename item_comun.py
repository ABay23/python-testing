
# * This is a commun intervew exercise
# * Find a value from list 1 in list 2.
# * First Approach is n**2 with 2 nested for loops

def item_in_common(list1, list2):
    for i in list1:
        for j in list2:
            if i == j:
                return True
    return False


list1 = [1, 3, 5]
list2 = [2, 4, 6]

print(item_in_common(list1, list2))
