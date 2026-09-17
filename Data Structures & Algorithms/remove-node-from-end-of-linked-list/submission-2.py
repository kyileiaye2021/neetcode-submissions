# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        pt1 = pt2 = dummy

        for i in range(n):
            pt1 = pt1.next

        while pt1 and pt1.next:
            pt1 = pt1.next
            pt2 = pt2.next

        to_remove = pt2.next
        next_new_node = to_remove.next
        pt2.next = next_new_node

        return dummy.next
