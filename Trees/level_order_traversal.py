class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        next_q = deque()

        out = []
        level = 0

        while root:
            if len(out) != level + 1:
                out.append([])
            out[level].append(root.val)
            if root.left: next_q.append(root.left)
            if root.right: next_q.append(root.right)

            if len(q) == 0:
                q = next_q
                next_q = deque()
                level += 1

            root = q.popleft() if len(q) > 0 else None
        return out
