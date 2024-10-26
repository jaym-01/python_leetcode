class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def solution(cur, min_val, max_val):
            if cur == None:
                return True
            elif cur.val > min_val and cur.val < max_val:
                return solution(cur.left, min_val, cur.val) and solution(cur.right, cur.val, max_val)
            else:
                return False

        return solution(root, -1 * inf, inf)
