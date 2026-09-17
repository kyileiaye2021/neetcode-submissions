# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
         
        # [1,2,3]
        # in preorder, first val always curr root node
        # if we node the num of left subtree from in order, we can differentiate left and right subtree


        # [2,1,3] 
        # find the index of curr root node
        # before curr root node is left subtree
        # after curr root node is right subtree

        # k = index of curr root
        # inorder[:k] is left subtree

        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0]) 
        k = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1:k+1], inorder[:k])
        root.right = self.buildTree(preorder[k+1:], inorder[k+1:])
        return root

