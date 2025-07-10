

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return f"[Node: {self.value}]"


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head

        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        node = Node(value)

        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None

        temp = self.head
        prev = self.head
        while temp.next:
            prev = temp
            temp = temp.next

        self.tail = prev
        self.tail.next = None
        self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        prev = self.head
        self.head = self.head.next
        prev.next = None
        self.length -= 1

        if self.length == 0:
            self.tail = None
        return prev

    def get(self, index):
        if index < 0 or index >= self.length:
            return None

        node = self.head
        for _ in range(index):
            node = node.next
        return node

    def set_value(self, index, value):
        node = self.get(index)
        if node:
            node.value = value
            return True
        return False

    def insert(self, index, value):
        if index > self.length or index < 0:
            return None
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)

        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()

        before = self.get(index - 1)
        node = before.next
        before.next = node.next
        node.next = None
        self.length -= 1
        return node

    def reverse(self):
        if self.length == 1:
            return

        temp = self.head
        self.head = self.tail
        self.tail = temp

        before = None
        after = temp.next
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after


ll = LinkedList(4)
ll.append(10)
ll.append(15)
ll.append(95)
ll.append(12)
ll.print_list()
ll.reverse()

print("\nAfter reversing")
ll.print_list()
