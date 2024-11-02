class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = root.val

        def solution(root):
            nonlocal max_sum
            if not root:
                return -1001
            else:
                l = solution(root.left)
                r = solution(root.right)

                max_sum = max(l, r, root.val + l + r, max_sum, root.val + l, root.val + r, root.val)

                return max(l + root.val, r + root.val, root.val)

        solution(root)

        return max_sum

class Solution:
    def helper(self, root):
        if root.left == None and root.right == None:
            return -10000, root.val
        elif root.right == None:
            nc, c = self.helper(root.left)
        elif root.left == None:
            nc, c = self.helper(root.right)
        else:
            l, lc = self.helper(root.left)
            r, rc = self.helper(root.right)
            val = root.val

            not_connected = max([l, r, rc, lc, lc + val + rc])
            connected = max([lc + val, rc + val, val])

            return not_connected, connected

        val = root.val
        not_connected = max([nc, c])
        connected = max([c + val, val])

        return not_connected, connected

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        return max(self.helper(root))
