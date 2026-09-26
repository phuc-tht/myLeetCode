# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        num1 = str(l1.val)
        num2 = str(l2.val)
        while l1.next:
            l1 = l1.next
            num1 = str(l1.val) + num1
        while l2.next:
            l2 = l2.next
            num2 = str(l2.val) + num2
        total = int(num1) + int(num2)
        head = ListNode(total % 10)
        total //= 10
        current = head
        while total > 0:
            current.next = ListNode(total % 10)
            current = current.next
            total //= 10
        return(head)
        