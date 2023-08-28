
# * This is how we build the Linked list

class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class CreateList:
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = + 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append_node(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop_item(self):
        if self.length == 0:
            return None
        temp = self.head
        prev = temp
        while temp.next:
            prev = temp
            temp = temp.next
        self.tail = prev
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = 0
            self.tail = 0
        return temp

    def prepend_item(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index >= self.length:
            return False
        if index == 0:
            self.prepend_item(value)
        elif index == self.length:
            self.append_node(value)

        new_node = Node(value)

        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.lenght += 1
        return True

    def remove_item(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first(index)
        elif index == self.length - 1:
            return self.pop_item(index)
        prev = self.get(index - 1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def reverse_list(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        prev = None
        after = temp.next
        for _ in range(self.length):
            after = temp.next
            temp.next = prev
            prev = temp
            temp = after


# * Testing
my_linked_list = CreateList(12)
my_linked_list.append_node(11)
my_linked_list.append_node(23)
my_linked_list.append_node(3)

# my_linked_list.set_value(2, 2)
# my_linked_list.remove_item(2)

my_linked_list.print_list()
my_linked_list.reverse_list()
my_linked_list.print_list()


# print(my_linked_list.get(2))
