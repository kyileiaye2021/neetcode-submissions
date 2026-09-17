# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # circular linked list
        # slow fast

        # greedy approach
        # first, second
        # traverse the first ahead n times
        # traverse the list with first and second until first becomes the last ele

        dummy = ListNode(0)
        dummy.next = head
        second = dummy
        first = head

        while n > 0:
            first = first.next
            n -= 1

        while first:
            second = second.next
            first = first.next

        second.next = second.next.next
        return dummy.next
        


