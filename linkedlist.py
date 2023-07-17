

# * This is how we build the Linked list

class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = + 1

    def print_list(self):
        temp = self.next
        while temp is not None:
            print(temp.valie)
            temp = temp.next

    def append_value(self):
        pass
