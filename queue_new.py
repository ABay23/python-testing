
# * As a concept queue on a linked list is O(1) if
# * we keep enqueueing from the last item on  a LList and
# *  Dequeueing formthe first item on the list
# *  Example: <--[22]->[4]->[13] <-- [46]

# * Node Class
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def enqueue(self, value):
        new_node = Node(value)

        # * this part is different, we validate based on an existing node with self.first
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1

    def dequeue(self):
        if self.length == 0:
            return None

        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp.next = None

        self.length -= 1
        return temp.value


my_queue = Queue(5)
my_queue.enqueue(33)
my_queue.enqueue(45)

my_queue.print()

print(my_queue.dequeue())
