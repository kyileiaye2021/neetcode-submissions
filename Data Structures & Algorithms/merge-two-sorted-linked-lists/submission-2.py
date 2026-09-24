# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # new list
        # i , j

        new_list = ListNode(0)
        curr = new_list

        i = list1
        j = list2

        while i and j:
            if i.val < j.val:
                curr.next = i
                i = i.next
                curr = curr.next

            else:
                curr.next = j
                j = j.next
                curr = curr.next

        if i:
            curr.next = i

        if j:
            curr.next = j

        return new_list.next