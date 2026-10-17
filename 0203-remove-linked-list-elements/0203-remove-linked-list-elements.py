# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        dummy = ListNode(0)
        dummy.next = head
        tail = dummy
        while tail.next is not None:
            if tail.next.val == val:
                tail.next = tail.next.next
            else:
                tail = tail.next
        return dummy.next