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
        
        dummy = ListNode(0)
        temp = dummy 
        carry = [0]

        while l1 and l2:
            
            if carry:
                sum = l1.val + l2.val + carry.pop()
            else:
                sum = l1.val + l2.val 
            div = sum // 10
            rem = sum % 10

            new_node = ListNode(rem)
            temp.next = new_node
            temp = temp.next

            carry.append(div)

            l1 = l1.next
            l2 = l2.next

        while l1:
            if carry:
                sum = l1.val + carry.pop()
            else:
                sum = l1.val
            div = sum // 10
            rem = sum % 10

            new_node = ListNode(rem)
            temp.next = new_node
            temp = temp.next
            carry.append(div)

            l1 = l1.next

        while l2:
            if carry:
                sum = l2.val + carry.pop()
            else:
                sum = l2.val 
            div = sum // 10
            rem = sum % 10

            new_node = ListNode(rem)
            temp.next = new_node
            temp = temp.next

            carry.append(div)
            
            l2 = l2.next

        if carry:
            rem = carry.pop()
            if rem != 0:
                new_node = ListNode(rem)
                temp.next = new_node
                temp = temp.next

        return dummy.next

        
            

