# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        slow, fast = dummy, head
        
        i = 0
        while i < n:
            fast = fast.next
            i += 1

        while fast:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return dummy.next

       # slow and fast pointer

       # fast pointer will go ahead of slow by n amount
       # go thru the list until the fast pointer reach the end

       # slow pointer next will point to slow pointer next next
       # return the head

       


