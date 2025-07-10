class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return f"[{self.value}]"


class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print(self):
        temp = self.first
        while temp:
            print(temp.value)
            temp = temp.next

    def enqueue(self, value):
        new_node = Node(value)
        if not self.first:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
        return True

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
        return temp


q = Queue(10)
q.enqueue(20)
q.enqueue(30)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
q.print()
