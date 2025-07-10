
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
            return True

        temp = self.root
        while True:
            if temp.value == value:
                return False

            if value < temp.value:
                if not temp.left:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if not temp.right:
                    temp.right = new_node
                    return True
                temp = temp.right
        return False

    def contains(self, value):
        temp = self.root
        while temp:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False



bst = BinarySearchTree()
bst.insert(100)
bst.insert(50)
bst.insert(70)
bst.insert(30)
bst.insert(200)

print(bst.root.left.left.value)
# print(bst.contains(100))
# print(bst.contains(200))
# bst.insert(200)
# bst.insert(200)
# print(bst.contains(200))