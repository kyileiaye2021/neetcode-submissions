# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # edge caes
        # l1 = [1, 2, 3], l2 = [9, 4, 0]
        # output: [0, 7, 3]
        
        
        carry = []
        dummy = ListNode()
        temp = dummy

        while l1 and l2:
            new_val = l1.val + l2.val
            if carry:
                new_val += carry.pop()

            rem = new_val % 10
            carry.append(new_val // 10)

            new_node = ListNode(rem)
            temp.next = new_node
            temp = temp.next

            l1 = l1.next
            l2 = l2.next

        while l1:
            new_val = l1.val 
            if carry:
                new_val += carry.pop()

            rem = new_val % 10
            carry.append(new_val // 10)

            new_node = ListNode(rem)
            temp.next = new_node
            temp = temp.next

            l1 = l1.next

        while l2:
            new_val = l2.val
            if carry:
                new_val += carry.pop()

            rem = new_val % 10
            carry.append(new_val // 10)

            new_node = ListNode(rem)
            temp.next = new_node
            temp = temp.next

            l2 = l2.next

        while carry:
            new_val = carry.pop()
            if new_val != 0:
                new_node = ListNode(new_val)
                temp.next = new_node
                temp = temp.next

        return dummy.next

            

            
            

