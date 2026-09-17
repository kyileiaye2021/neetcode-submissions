# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # first we have to find the node in the tree
        # if found, we have 3 options
        # if the removed node has no children, 
        #   return null
        # if the removed node has left child
        #   removed node becomes left child
        # if the removed node has right child
        #   removed node becomes right child

        if not root:
            return root

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)

        else:
            if not root.left and not root.right:
                return None
            
            elif not root.right:
                return root.left

            elif not root.left:
                return root.right

            else:
                cur = root.right

                while cur.left:
                    cur = cur.left
                
                root.val = cur.val # replace the root val with successor val
                root.right = self.deleteNode(root.right, cur.val) # delete the successor node

        return root