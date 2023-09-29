

class HashTable:
    def __init__(self, key=7):
        self.my_table = [None] * key

    def _hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.my_table)
        return my_hash

    def _print(self):
        for i, val in enumerate(self.my_table):
            print(i, ':', val)

    def _set_item(self, key, value):
        index = self._hash(key)
        if self.my_table[index] == None:
            self.my_table[index] = []
        self.my_table[index].append([key, value])

    # def _get_item(self, key):
    #     index = self._hash(key)
    #     if self.my_table[index] is not None:
    #         for i in range(len(self.my_table[index])):
    #             if self.my_table[index][i][0] == key:
    #                 return self.my_table[index][i][1]
    #     return False

    def get_item(self, key):
        index = self._hash(key)
        if self.my_table[index] is not None:
            for i in range(len(self.my_table[index])):
                if self.my_table[index][i][0] == key:
                    return self.my_table[index][i][1]
        return False

    def _keys(self):
        all_keys = []
        for i in range(len(self.my_table)):
            if self.my_table[i] is not None:
                for j in range(len(self.my_table[i])):
                    all_keys.append(self.my_table[i][j][0])
        return all_keys


the_hash = HashTable(10)

print(the_hash.my_table)
hax = the_hash._hash('Dog')
print(hax)
the_hash._set_item('Wolf', 2300)
the_hash._set_item('Whale', 800)

the_hash._set_item('Jiraff', 200)
the_hash._set_item('Shark', 5000)

# the_hash._print()
print(the_hash.get_item('Wolf'))
print(the_hash.get_item('Jiraff'))
print(the_hash.get_item('Shark'))

print(the_hash._keys())
the_hash._print()
