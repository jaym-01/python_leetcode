class Solution:
    # storing greatest value -> if greater than that -> nothing greater than it
    def goodNodes(self, root: TreeNode) -> int:
        def solution(cur, max_val):
            if cur == None:
                return 0
            else:
                count = 1 if cur.val >= max_val else 0

                count += solution(cur.left, max(max_val, cur.val))
                count += solution(cur.right, max(max_val, cur.val))

                return count
        
        return solution(root, root.val)
