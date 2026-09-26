# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        # recur(preorder, inorder)
        #   if len(preorder) == 0 and len(inorder) == 0:
        #       return None

        # res = create a node for preorder[0]
        # get index of preorder[0]
        # res.left = call left subtree (preorder[1:index+1], inorder[:index])
        # res.right = call right subtree (preorder[index+1:], inorder[index + 1: ])
        # return res
        
        indices = {val: idx for idx, val in enumerate(inorder)}
        preorder_idx = 0
        def recur_buildTree(left, right):

            nonlocal preorder_idx 
            if left > right:
                return None

            # res = TreeNode(preorder[0])
            # index = indices[preorder[0]]
            # res.left = recur_buildTree(preorder[1:index + 1], inorder[:index])
            # res.right = recur_buildTree(preorder[index + 1:], inorder[index + 1:])
            # return res

            root_val = preorder[preorder_idx]
            mid = indices[root_val]
            root = TreeNode(root_val)
            preorder_idx += 1
            root.left = recur_buildTree(left, mid - 1)
            root.right = recur_buildTree(mid + 1, right)

            return root
            

        return recur_buildTree(0, len(inorder) - 1)