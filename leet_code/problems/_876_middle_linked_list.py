# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        slow_pointer = fast_pointer = head

        if not fast_pointer.next:
            return head
        if not head:
            return None

        while fast_pointer:
            if not fast_pointer.next:
                return slow_pointer
            fast_pointer = fast_pointer.next.next
            slow_pointer = slow_pointer.next
