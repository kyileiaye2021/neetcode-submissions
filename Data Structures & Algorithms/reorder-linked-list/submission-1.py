# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # [0,1,2,3,4,5,6]
        # [0,1,2,3,6,5,4]
        # [0,6,1,5,2,4,3]

        # slow - fast pointer
        # separate two linked list
        # dummy node

        # after getting slow (mid)
        # head2 = slow.next
        # set slow next = none
        # start from the heads of the two linked list
        #   add head1 to dummy 
        #   add head2 to dummy 
        #   move head1 to its next
        #   move head2 to its next

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        head2 = slow.next
        prev = None
        while head2:
            next_node = head2.next
            head2.next = prev
            prev = head2
            head2 = next_node

        slow.next = None

        dummy = ListNode(0)
        curr = dummy

        while head and prev:
            curr.next = head
            curr = curr.next
            head = head.next

            curr.next = prev
            curr = curr.next
            prev = prev.next

        while head:
            curr.next = head
            curr = curr.next
            head = head.next

        while prev:
            curr.next = prev
            curr = curr.next
            prev = prev.next


        



        
      










