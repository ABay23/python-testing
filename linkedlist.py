

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

    def append_value(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def pop_value(self) -> None:
        if self.length == 0:
            return None
        prev = self.head
        temp = self.head
        while temp is not None:
            prev = temp
            temp = self.next
        self.tail = prev
        self.tail.next = None
        self.length -= 1
        return temp


my_linked_list = LinkedList(1)
my_linked_list = LinkedList.append_value(2)
my_linked_list = LinkedList.print_list()
