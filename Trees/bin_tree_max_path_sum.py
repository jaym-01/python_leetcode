# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
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
