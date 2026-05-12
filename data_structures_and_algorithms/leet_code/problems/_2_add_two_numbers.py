# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        dummy = ListNode()
        current = dummy 
        carry = 0

        while (l1 or l2) or carry:
            if l1:
                l1_val = l1.val
            else:
                l1_val = 0
            if l2:
                l2_val=l2.val
            else:
                l2_val = 0
            sum_ = l1_val + l2_val + carry
            carry = sum_//10
            digit = sum_%10
            current.next = ListNode(digit)
            current = current.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return dummy.next



