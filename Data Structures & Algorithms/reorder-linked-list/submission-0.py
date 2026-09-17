# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # happy case
        # Input: head = [2,4,6,8]
        # Output: [2,8,4,6]

        # input: head = [2, 4, 6, 8, 10]
        # Output: [2, 10, 4, 8, 6]

        # input: head = [1, 2, 6]
        # output: [1, 6, 2]

        # edge case
        # input: head = [1]
        # output: [1]

        # input: head = [2, 5]
        # output :[2, 5]

        # create a reverse order list
        # iterate thru the two list sim
        #   adding the ele alternatively 

        # create a new list container
        # iterate thru the list with two pointers
        # create nodes and with l and r pointer ele and create a linked list

        # fast and slow pointer

        slow,fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        curr = slow.next
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        slow.next = None

        while head and prev:
            prev_next = prev.next
            head_next = head.next
            prev.next = head.next
            head.next = prev
            head = head_next
            prev = prev_next

        
            

        










