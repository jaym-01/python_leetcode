# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(inorder) == 0:
            return None
        elif len(inorder) == 1:
            return TreeNode(inorder[0])
        else:
            root_val = preorder[0]
            root_node = TreeNode(root_val)

            l_preorder = []
            r_preorder = []
            l_inorder = []
            r_inorder = []

            for i in range(len(inorder)):
                if root_val == inorder[i]:
                    l_inorder = inorder[:i]
                    if i + 1 < len(inorder):
                        r_inorder = inorder[i+1:]

                    l_preorder = preorder[1:len(l_inorder) + 1]
                    if len(r_inorder) > 0:
                        r_preorder = preorder[len(l_inorder) + 1:]
            
            root_node.left = self.buildTree(l_preorder, l_inorder)
            root_node.right = self.buildTree(r_preorder, r_inorder)
        
            return root_node
                    

