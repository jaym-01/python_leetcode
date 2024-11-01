class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        out = []

        def traverse(cur, cur_h, min_h):
            nonlocal out
            if cur == None:
                return 0
            else:
                if cur_h > min_h:
                    out.append(cur.val)

                r = traverse(cur.right, cur_h + 1, min_h)
                l = traverse(cur.left, cur_h + 1, max(min_h, cur_h + r))

                return max(l, r) + 1
        
        traverse(root, 0, -1)

        return out
