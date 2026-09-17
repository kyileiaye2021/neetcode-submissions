# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
        
        # diameter: longest path between two nodes 
        # happy cases
        #       3
        #      / \
        #     2   8
        #        / \
        #       4.  9
        #.       \    \
        #         5    11
        # output: 4

        #       3
        #      / \
        #     2   8
        # output: 2

        # edge cases
        # input: None
        # output: None

        # input: 3
        # output: 0

        #       3
        #      / 
        #     2   
        # output: 1

        # goal : find the longest path between two nodes
        #        it can be in left subtrees and right subtrees

        # # DFS
        # update the diameter 
        # update the height of the subtree (need to take max)

        # the sum of the max height of left subtree and height of right subtree
        # base case
        # if the node is none
        # return 0
        
        # recursive call on left subtree and update the curr height of the subtree
        # recursive call on right subtree and update the curr height of the subtree
        
        # get the sum and return 

    def diameter_helper(self, root, diameter_res):
        # base case
        if not root:
            return 0

        left_height = self.diameter_helper(root.left, diameter_res)
        right_height = self.diameter_helper(root.right, diameter_res)

        # update the diameter of the tree
        diameter_res[0] = max(diameter_res[0], (left_height + right_height))

        # update the height of the tree (need to take max between left and right)
        return 1 + max(left_height, right_height) 
        
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = [0]
        self.diameter_helper(root, diameter)
        return diameter[0]







