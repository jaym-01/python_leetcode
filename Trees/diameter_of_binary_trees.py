class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def solution(root: Optional[TreeNode]) -> tuple[int, int]:
            if root == None:
                return 0, 0
            else:            
                lnc = 0
                lc = 0
                rnc = 0
                rc = 0

                if root.left != None:
                    lnc, lc = solution(root.left)
                    lc += 1
                
                if root.right != None:
                    rnc, rc = solution(root.right)
                    rc += 1

                nc = max(lnc, rnc, lc + rc)
                c = max(lc, rc)

                return nc, c
        return max(solution(root))
