# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # new list
        # i , j

        # recur(list1, list2)
        # base case
        # if list1 is empty: return list2
        # if list2 is empty, return list1 
        # recursive case
        # if list1.val < list2.val
        #   list1.next = recur(list1.next, list2)
        # else
        #   list2.next = recur(list1, list2.next)

        def recur(list1, list2):
            if not list1:
                return list2

            if not list2:
                return list1

            if list1.val < list2.val:
                list1.next = recur(list1.next, list2)
                return list1

            else:
                list2.next = recur(list1, list2.next)
                return list2

        return recur(list1, list2)



        # new_list = ListNode(0)
        # curr = new_list

        # i = list1
        # j = list2

        # while i and j:
        #     if i.val < j.val:
        #         curr.next = i
        #         i = i.next
        #         curr = curr.next

        #     else:
        #         curr.next = j
        #         j = j.next
        #         curr = curr.next

        # if i:
        #     curr.next = i

        # if j:
        #     curr.next = j

        # return new_list.next