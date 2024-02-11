class Solution:
    def maxPathSum(self, root) -> int:
        x1, x2 = self.helper(root)

        return max(x1, x2)

    def helper(self, root):
        if root == None:
            return -1001, -1001
        lwc, lwtc = self.helper(root.left)
        rwc, rwtc = self.helper(root.right)

        tmp2 = max(root.val + lwc, root.val + rwc)
        wr = max(root.val, tmp2)

        tmp1 = max(lwtc, rwtc)
        tmp2 = max(lwc, rwc)
        tmp3 = max(tmp1,root.val + lwc + rwc)
        wtr = max(tmp3, tmp2)

        return wr, wtr