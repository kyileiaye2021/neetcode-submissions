# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root):
        # base case:
        if not root:
            return [0, 0]

        # post order traversal so need to call left and right subtree first
        left_subtree = self.dfs(root.left)
        right_subtree = self.dfs(root.right)

        withRoot = root.val + left_subtree[1] + right_subtree[1]
        withoutRoot = max(left_subtree) + max(right_subtree)

        return [withRoot, withoutRoot]

    def rob(self, root: Optional[TreeNode]) -> int:
        # happy case
        # input: 1
        # output: 1

        # input: 1
        #       / 
        #      2
        #     /
        #    3
        # output: 1 + 3 = 4

        # input: 1
        #       / \
        #      2.  4
        #     / \
        #    1   9
        # disconnect after 1
        # 1 + 1 + 9 = 11

        # input; 1
        #       / \
        #      2.  4
        #     / \   \
        #    1   9    8
        # disconnect after 1
        # 1 + 1 + 9 + 8 = 19

        # # bfs
        # # create a queue
        # # add the nodes in the queue until we encounter break
        # # if we encounter break, we add the popped node ele to the max_money
        # # go to the next nodes
        # # if the node has children, we add the  children nodes to the queue
        # # else: add the nodes to the max_money
        # # how can we do the break between two-directly linked houses

        # queue = collections.deque()
        # queue.append(root)

        # max_money = 0

        # while queue:

        #     queue_len = len(queue)

        #     curr_node = queue.popleft()
        #     # everytime we meet the alert, add the nodes to the max_money
        #     if not curr_node.left and not curr_node.right:
        #         print(curr_node.val)
        #         max_money += curr_node.val 

        #     if curr_node.left:
        #         queue.append(curr_node.left)

        #     if curr_node.right:
        #         queue.append(curr_node.right)

        # return max_money

        #dfs 
        # we can't go to the adjacent nodes
        # post order traversal
        # in each subtree
        # return [withRoot, withoutRoot]
        # we have to see what max val the subtree will return with root taken and without root taken
        # base case: if the node is null --> [0,0]
        # withRoot = curr root val + leftsubtree's withoutRoot max val + rightSubtree's withoutRoot max val
        # withoutRoot = get max val of leftsubtree + max val of rightsubtree
        # return [withRoot, withoutRoot]

        return max(self.dfs(root))








