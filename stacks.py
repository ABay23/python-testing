class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1

    def pop(self):
        if self.height == 0:
            return None

        temp = self.top
        self.top = temp.next
        self.height -= 1
        return temp.value


my_stack = Stack(6)
my_stack.push(11)
my_stack.push(22)
my_stack.push(4)

my_stack.print()

print(my_stack.pop())
print(my_stack.pop())

my_stack.push(23)
my_stack.print()
