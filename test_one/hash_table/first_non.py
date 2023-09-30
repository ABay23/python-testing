def first_non_repeating_char(str):
    my_table = {}

    for c in str:
        if c in my_table:
            my_table[c] = my_table[c] + 1
        else:
            my_table[c] = 1
    for c in str:
        if my_table[c] == 1:
            return c

    return None


print(first_non_repeating_char('leetcode'))

print(first_non_repeating_char('hello'))

print(first_non_repeating_char('aabbcc'))


"""
    EXPECTED OUTPUT:
    ----------------
    l
    h
    None

"""
