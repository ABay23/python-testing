class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.rigth = None


class NewTree:
    def __init__(self):
        self.root = None

    def _insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True

        temp = self.root
        while (True):

            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            if new_node.value > temp.value:
                if temp.rigth is None:
                    temp.rigth = new_node
                    return True
                temp = temp.rigth

    def _contains(self, value):
        temp = self.root

        while temp is not None:
            if value < temp.value:
                temp = temp.left
            if value > temp.value:
                temp = temp.rigth
            return True
        return False
# * We need to create a Tree for this exercise of recursion
# * Now we are going to add the recursive function to validate

    def __r_contains(self, current_node, value):
        if current_node == None:
            return False
        if value == current_node.value:
            return True
        if value < current_node.value:
            return self.__r_contains(current_node.left, value)
        if value > current_node.value:
            return self.__r_contains(current_node.rigth, value)

    def r_contains(self, value):
        return self.__r_contains(self.root, value)


n_tree = NewTree()
n_tree._insert(47)
n_tree._insert(21)
n_tree._insert(18)
n_tree._insert(27)
n_tree._insert(76)
n_tree._insert(52)
n_tree._insert(82)

print('BST Contains 27:')
print(n_tree.r_contains(27))

print('\nBST Contains 27:')
print(n_tree.r_contains(17))


# print(n_tree.root.value)
# print(n_tree.root.left.value)
# print(n_tree.root.rigth.value)
