# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        # Create a dummy node
        dummy = ListNode(0)
        dummy.next = head
        slow = dummy
        fast = dummy
        
        # Move fast n+1 steps ahead
        for _ in range(n + 1):
            fast = fast.next
        
        # Move both pointers until fast reaches the end
        while fast:
            slow = slow.next
            fast = fast.next
        
        # Remove the nth node
        slow.next = slow.next.next
        
        return dummy.next
