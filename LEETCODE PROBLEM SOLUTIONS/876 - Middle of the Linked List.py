# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: [ListNode]) -> [ListNode]:
        count = 0
        current = head

        while current:
            count += 1
            current = current.next

        current = head

        for i in range(count // 2):
            current = current.next
        return current



class Solution(object):
    def middleNode(self, head):
        slow_pointer = head
        fast_pointer = head

        while fast_pointer is not None and fast_pointer.next is not None:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next

        return slow_pointer

