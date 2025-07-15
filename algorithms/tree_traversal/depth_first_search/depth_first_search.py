from data_structures.tree.binary_search_tree import BinarySearchTree


class BST(BinarySearchTree):
    def __init__(self):
        self.root = None
        super()

    def depth_first_search_preorder(self):
        results = []
        def traverse(current_node):
            results.append(current_node.value)

            if current_node.left:
                traverse(current_node.left)
            if current_node.right:
                traverse(current_node.right)

        traverse(self.root)
        return results

    def depth_first_search_postorder(self):
        results = []
        def traverse(current_node):
            if current_node.left:
                traverse(current_node.left)
            if current_node.right:
                traverse(current_node.right)
            results.append(current_node.value)

        traverse(self.root)
        return results

    def depth_first_search_inorder(self):
        results = []
        def traverse(current_node):
            if current_node.left:
                traverse(current_node.left)

            results.append(current_node.value)

            if current_node.right:
                traverse(current_node.right)


        traverse(self.root)
        return results






if __name__ == "__main__":
    bst = BST()
    bst.insert(47)
    bst.insert(21)
    bst.insert(76)
    bst.insert(18)
    bst.insert(27)
    bst.insert(52)
    bst.insert(82)

    print(bst.depth_first_search_preorder())
    print(bst.depth_first_search_postorder())
    print(bst.depth_first_search_inorder())
