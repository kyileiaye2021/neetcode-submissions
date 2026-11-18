# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        # happy cases
        # 1 -> 2 -> 3 -> 4 -> 5
        # 2, 3
        # 1 -> 3 -> 2 -> 4 -> 5

        # 1 -> 2 -> 3 -> 4 -> 5
        # 1,2
        # 2 -> 1 -> 3 -> 4 -> 5

        # 1 -> 2 -> 3 -> 4 -> 5
        # 4, 5
        # 1 -> 2 -> 3 -> 5 -> 4

        # edge cases
        # 1 
        # 1, 1
        # 1

        # 1 -> 2
        # 1, 1
        # 1 -> 2

        # use dummy node and connect head to dummy
        # find the left and right point in the list
        # keep track of the nodes before/after the left and right
        # reverse the list nodes between left and right
        # connect left and right back to the reverse list

        dummy = ListNode(0)
        dummy.next = head
        l, r = dummy, dummy
        l_before = None

        for _ in range(right - left):
            r = r.next

        for _ in range(left):
            l_before = l
            l = l.next
            r = r.next

        r_after = r.next

        # reverse the sublist between l and r
        prev = None
        curr = l
        while prev != r:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        
        start = l_before.next
        end = prev

        l_before.next = end
        start.next = r_after

        return dummy.next

        

        




        