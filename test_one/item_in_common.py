def item_in_common(list1, list2):
    check_list = {}

    for i in list1:
        check_list[i] = True

    for j in list2:
        if j in check_list:
            return j, check_list[j]

    return False


L1 = [2, 4, 8]
L2 = [7, 8, 4]

print(item_in_common(L1, L2))
