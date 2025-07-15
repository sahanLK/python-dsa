
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


    """
    Recursive Contains Methods
    """
    def __r_contains(self, current_node, value):
        if current_node == None:
            return False
        if value == current_node.value:
            return True
        if value < current_node.value:
            return self.__r_contains(current_node.left, value)
        if value > current_node.value:
            return self.__r_contains(current_node.right, value)

    def r_contains(self, value):
        return self.__r_contains(self.root, value)

    """
    Recursive Insert Methods
    """
    def __r_insert(self, current_node, value):
        if not current_node:
            return Node(value)
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)
        if value > current_node.value:
            current_node.right = self.__r_insert(current_node.right, value)
        return current_node

    def r_insert(self, value):
        if not self.root:
            self.root = Node(value)
        self.__r_insert(self.root, value)


    """
    Recursive Delete Methods
    """
    def min_value(self, current_node):
        while current_node.left:
            current_node = current_node.left
        return current_node.value

    def __r_delete(self, current_node, value):
        if current_node == None:
            return None

        if value < current_node.value:
            current_node.left = self.__r_delete(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self.__r_delete(current_node.right, value)
        else:
            if current_node.left == None and current_node.right == None:
                return None
            elif current_node.left == None:
                current_node = current_node.right
            elif current_node.right == None:
                current_node = current_node.left
            else:
                sub_tree_min = self.min_value(current_node.right)
                current_node.value = sub_tree_min
                current_node.right = self.r_delete(current_node.right, sub_tree_min)
        return current_node

    def r_delete(self, value):
        self.__r_delete(self.root, value)


if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.r_insert(10)
    bst.r_insert(5)
    bst.r_insert(20)
    bst.r_insert(30)
    bst.insert(100)
    bst.insert(50)
    bst.insert(70)

    bst.r_delete(30)
    print(bst.contains(30))