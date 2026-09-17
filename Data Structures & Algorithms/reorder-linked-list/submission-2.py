# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # fast and slow pointers
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        cur = slow.next
        slow.next = None
        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node

        dummy = ListNode()
        cur = dummy

        while head and prev:
            cur.next = head
            cur = cur.next
            head = head.next

            cur.next = prev
            cur = cur.next
            prev = prev.next

        while head:
            cur.next = head
            cur = cur.next
            head = head.next

        while prev:
            cur.next = prev
            cur = cur.next
            prev = prev.next

    




        

