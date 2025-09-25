# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        dummy.next = head
        prev_group = dummy

        while True:
            # Find the kth node
            kth = prev_group
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next  # less than k nodes left, stop

            group_next = kth.next

            # Reverse group
            prev, curr = kth.next, prev_group.next
            while curr != group_next:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            # Reconnect reversed group
            tmp = prev_group.next
            prev_group.next = kth
            prev_group = tmp
