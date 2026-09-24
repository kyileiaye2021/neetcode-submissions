# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # list 
        # O(n) time O(n) space

        # stack 
        # O(n) time and O(n) space

        # find middle point
        # split the linked list into 2
        # O(n) time O(1) space
        def recur_reverse(curr, prev):
            # base case
            if not curr:
                return prev
            # recursive step
            next_node = curr.next
            curr.next = prev
            return recur_reverse(next_node, curr)

        def recur_merged(head, reversed, is_head):
            # base case
            if not head:
                return reversed

            if not reversed:
                return head

            # recursive step
            if is_head:
                head.next = recur_merged(head.next, reversed, False)
                return head
            else:
                reversed.next = recur_merged(head, reversed.next, True)
                return reversed

        slow = head
        fast = head

        # find middle node
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        curr = slow.next
        slow.next = None

        # reverse the second sub list
        prev = None
        reversed = recur_reverse(curr, prev)


        # merging two linked list
        recur_merged(head, reversed, True)
        # dummy = ListNode()
        # res = dummy
        # temp = head
        # while temp and prev:
        #     res.next = temp
        #     res = res.next
        #     temp = temp.next
        #     res.next = prev
        #     res = res.next
        #     prev = prev.next

        # if temp:
        #     res.next = temp
        
        # if prev:
        #     res.next = prev 

    

