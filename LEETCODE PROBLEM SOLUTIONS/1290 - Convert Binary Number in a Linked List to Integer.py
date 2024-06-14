# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        answer = ''
        if head is None:
            return

        current = head
        while current:
            answer = answer + str(current.val)
            current = current.next
        return int(answer, 2)