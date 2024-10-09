class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []

        def solution(cur: Optional[TreeNode]) -> Optional[TreeNode]:
            if cur == None:
                return -1
            elif len(stack) == k:
                return stack[-1]
            else:
                solution(cur.left)
                stack.append(cur.val)
                solution(cur.right)
        solution(root)
        return stack[k-1]
