class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = True

        def check_balance(root):
            nonlocal balanced
            if not balanced:
                return 1
            elif root is None:
                return 0
            else:
                l = check_balance(root.left) + 1
                r = check_balance(root.right) + 1

                if not balanced:
                    return max(l, r)
                else:
                    balanced &= (abs(l - r) < 2)
                    print(abs(l - r), balanced)
                    return max(l, r)

        check_balance(root)
        return balanced


