
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return f"[{self.value}]"


class Stack:
    def __init__(self, value):
        node = Node(value)
        self.top = node
        self.height = 1

    def print(self, reverse = False):
        temp = self.top
        lst = ""
        while temp:
            lst += f"{'<-' if reverse else ''} [{temp.value}] {'->' if not reverse else ''}"
            temp = temp.next if not reverse else temp.prev
        print(lst)

    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1
        return True

    def pop(self):
        if self.height == 0:
            return None
        
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -= 1
        return temp


s = Stack(10)
s.push(20)
# s.push(30)
s.pop()
s.print()