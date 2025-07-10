
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __repr__(self):
        return f"[{self.value}]"


class DoublyLinkedList:
    def __init__(self, value):
        node = Node(value)
        self.head = node
        self.tail = node
        self.length = 1

    def print_list(self, reverse: bool = False):
        temp = self.head if not reverse else self.tail
        lst = ""
        while temp:
            lst += f"{'<-' if reverse else ''} [{temp.value}] {'->' if not reverse else ''}"
            temp = temp.next if not reverse else temp.prev
        print(lst)

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        temp = self.tail
        if self.length <= 1:
            self.head = None
            self.tail = None
        else:
            self.tail.prev.next = None
            self.tail = self.tail.prev
        self.length -= 1
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        temp = self.head
        if self.length <= 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None

        temp = self.head
        if index < self.length / 2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - (index + 1)):
                temp = temp.prev
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False

        if index == 0:
            self.prepend(value)
            return True

        if index == self.length:
            self.append(value)
            return True

        new_node = Node(value)
        before = self.get(index - 1)
        after = before.next

        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index > self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()

        node = self.get(index)
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = None
        node.prev = None
        self.length -= 1
        return node



dll = DoublyLinkedList(0)
dll.append(1)
dll.append(2)

print("Removed: ", dll.remove(1))
dll.print_list()


