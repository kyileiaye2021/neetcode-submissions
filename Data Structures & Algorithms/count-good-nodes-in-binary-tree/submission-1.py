# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, root, max_node, count):
        if not root:
            return 
        
        print(f"root val: {root.val}, max_node: {max_node}")
        if root.val >= max_node:
            count[0] += 1
            max_node = root.val

        self.dfs(root.left, max_node, count)
        self.dfs(root.right, max_node, count)

    def goodNodes(self, root: TreeNode) -> int:
        # happy cases
        # input: root: 2
        #             / \
        #             1  3
        # output: [2, 3] return 2

        # input: root: 1
        #             / \
        #             5. 9
        # output: [1, 5, 9] return 3

        # input: root: 4
        #              /\
        #             -1 -4
        #             /   \
        #             5.  -2
        # output: 2

        # edge cases
        # input: root: 1
        # output: 1

        # dfs
        # base case: if the node is null
        # return 

        # if the node is greater than the max node, increment the count 
        # maintain the max node val within the path
        # go to left subtree
        # go to right subtree
        max_node = float('-inf')
        count = [0]
        self.dfs(root, max_node, count)
        return count[0]

