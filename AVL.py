class Tree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1

class AVL:
    def __init__(self):
        self.root: Tree = None

    def insert_node(self, val):
        self.root = self._insert_helper(self.root, val)

    def _insert_helper(self, root, val):
        if not root:
            return Tree(val)
        elif root.val > val:
            root.left = self._insert_helper(root.left, val)
        else:
            root.right = self._insert_helper(root.right, val)

        root.height = 1 + max(self._getHeight(root.right), self._getHeight(root.left))

        bf = self._getBF(root)

        if bf > 1:
            if self._getBF(root.left) < 0:
                root.left = self.leftr(root.left)
            return self.rightr(root)
        elif bf < -1:
            if self._getBF(root.right) > 0:
                root.right = self.rightr(root.right)
            return self.leftr(root)
        else:
            return root

    def _getBF(self, node):
        if not node:
            return 0
        else:
            return self._getHeight(node.left) - self._getHeight(node.right)

    def _getHeight(self, node: Tree | None):
        if not node:
            return 0
        else:
            return node.height

    def leftr(self, root):
        A = root
        root = root.right # changing B to the root
        BL = root.left

        # making swaps
        A.right = BL
        root.left = A
        
        return root
        

    def rightr(self, root):
        A = root
        root = root.left
        BR = root.right

        A.left = BR
        root.right = A

        return root


    def print_tree(self):
        return self._print_helper(self.root, 0)
    def _print_helper(self, root: Tree, step):
        if not root:
            return
        else:
            print("".join([" "]*step) + str(root.val))
            if root.left or root.right:
                print("".join([" "]*step) + "{")
                self._print_helper(root.left, step + 2)
                self._print_helper(root.right, step + 2)
                print("".join([" "]*step) + "}")


if __name__ == "__main__":
    test = AVL()

    test.insert_node(1)
    test.insert_node(2)
    test.insert_node(3)
    test.insert_node(4)
    test.insert_node(5)
    test.insert_node(0)

    test.print_tree()