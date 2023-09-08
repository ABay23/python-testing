
# * this is the constructor for a Binary Tree

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# * This is the standar constructor for a new tree with a node
class BinarySearchTree:
    def __init__(self, value):
        new_node = Node(value)

        # * We have to create a pointer for the first node to be able to access it called 'root'
        self.root = new_node

# * In this version  of a binary tree, we create an empty tree and we insert the first node later.
# * That is the reason why we assign None to root.
# * Is the one we are going to use mooving forward


class BinarySearchTreeB:
    def __init__(self):
        self.root = None

# * Insert Method
    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True

        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left == None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right == None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        # * This validation is not needed because the value None breaks the loop and returns False.
        # if self.root is None:
        #     return False
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False


my_tree = BinarySearchTreeB()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print(my_tree.contains(27))
print(my_tree.contains(17))

# print(my_tree.root.value)
# print(my_tree.root.left.value)
# print(my_tree.root.right.value)
