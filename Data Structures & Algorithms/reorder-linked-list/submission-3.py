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

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        curr = slow.next
        slow.next = None

        # reverse the second sub list
        prev = None
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        dummy = ListNode()
        res = dummy
        temp = head
        while temp and prev:
            res.next = temp
            res = res.next
            temp = temp.next
            res.next = prev
            res = res.next
            prev = prev.next

        if temp:
            res.next = temp
        
        if prev:
            res.next = prev 

    

