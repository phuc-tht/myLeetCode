# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        ans_num = 0
        for lst in [l1, l2]:
            cur = lst
            arr = []
            string = ""
            while cur is not None:
                arr.append(cur.val)
                cur = cur.next
            for i in reversed(arr):
                string += str(i)
            ans_num += int(string)
        ans_list = []
        for i in str(ans_num):
            ans_list.insert(0, int(i))
        head = ListNode(0)
        cur = head
        for i in ans_list:
            cur.next = ListNode(i)
            cur = cur.next
        ans = head.next 
        return(ans)
        