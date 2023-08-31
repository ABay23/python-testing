
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Linked_List:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = + 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length = + 1

    def print(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def pop(self):
        if self.length == 0:
            return None
        else:
            temp = self.head
            pr = self.head
            while temp.next:
                pr = temp
                temp = temp.next
            pr.next = None
            self.tail = pr
            self.length = - 1
            if self.length == 0:
                self.head = None
                self.tail = None
            return temp

    def prepend(self):
        pass

    def pop_first(self):
        pass


my_new_list = Linked_List(6)
my_new_list.append(4)
my_new_list.append(5)
# my_new_list.append(10)

my_new_list.print()

my_new_list.pop()

my_new_list.print()
