# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution: 
    def merge(self, curr1, curr2):
        dummy = temp = ListNode(0)

        while curr1 and curr2:
            if curr1.val > curr2.val:
                temp.next = curr2
                curr2 = curr2.next

            else:
                temp.next = curr1
                curr1 = curr1.next
            
            temp = temp.next

        if curr1:
            temp.next = curr1
            temp = temp.next

        if curr2:
            temp.next = curr2
            temp = temp.next

        curr2 = dummy.next
        return curr2


    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        # iterate thru the list upto n-1 time
        #   dummy node
        #   add to the res list based on the sorting val of curr list and next list
        #   replace the second list with the new dummy list

        # compare the second to last list and the last list

        if not lists:
            return None
        
        while len(lists) > 1:
            mergedList = []

            for i in range(0, len(lists), 2): # merging two linked lists at a time
                curr1 = lists[i]
                curr2 = lists[i + 1] if i + 1 < len(lists) else None
                mergedList.append(self.merge(curr1, curr2)) # storing all merged lists into a list

            lists = mergedList  # we will merge the merged list again

        return lists[0]


            




