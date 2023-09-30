# def group_anagrams(strings):
#     anagram_groups = {}
#     for string in strings:
#         canonical = ''.join(sorted(string))
#         if canonical in anagram_groups:
#             anagram_groups[canonical].append(string)
#         else:
#             anagram_groups[canonical] = [string]
#     return list(anagram_groups.values())


# print("1st set:")
# print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

# print("\n2nd set:")
# print(group_anagrams(["abc", "cba", "bac", "foo", "bar"]))

# print("\n3rd set:")
# print(group_anagrams(
#     ["listen", "silent", "triangle", "integral", "garden", "ranged"]))


"""
    EXPECTED OUTPUT:
    ----------------
    1st set:
    [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

    2nd set:
    [['abc', 'cba', 'bac'], ['foo'], ['bar']]

    3rd set:
    [['listen', 'silent'], ['triangle', 'integral'], ['garden', 'ranged']]

"""


def anagram_gp(string):
    da_table = {}
    out = []
    for w in string:
        canonical = ''.join(sorted(w))
        if canonical in da_table:
            da_table[canonical].append(w)
        else:
            da_table[canonical] = [w]
    return da_table.values()


# print(
print(anagram_gp(["eat", "tea", "tan", "ate", "nat", "bat"]))
# )

print(anagram_gp(["abc", "cba", "bac", "foo", "bar"]))
