# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        length = 0
        current = head
        while current is not None:
            length += 1
            current = current.next
        dummy = ListNode(0, head)
        prev = dummy

        for _ in range(length - n):
            prev = prev.next
        prev.next = prev.next.next
        
        return dummy.next