# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        num = 0
        factor = 1
        while l1:
            num += l1.val * factor
            factor *= 10
            l1 = l1.next
        factor = 1
        while l2:
            num += l2.val * factor
            factor *= 10
            l2 = l2.next
        if num == 0:
            return(ListNode(0))
        head = ListNode(0)
        current = head
        while num > 0:
            current.next = ListNode(num % 10)
            num //= 10
            current = current.next
        return(head.next)
        