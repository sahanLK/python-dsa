from data_structures.tree.binary_search_tree import BinarySearchTree


class BST(BinarySearchTree):
    def __init__(self):
        self.root = None
        super()
    def breadth_first_search(self):
        queue = [self.root]
        output = []

        while queue:
            item = queue.pop(0)
            output.append(item.value)

            if item.left:
                queue.append(item.left)
            if item.right:
                queue.append(item.right)
        return output



if __name__ == "__main__":
    bst = BST()
    bst.insert(47)
    bst.insert(21)
    bst.insert(76)
    bst.insert(18)
    bst.insert(27)
    bst.insert(52)
    bst.insert(82)

    print(bst.breadth_first_search())
