#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# class Solution:
#     def swapPairs(self, head: ListNode) -> ListNode:

head = ListNode(1)
v1 = ListNode(2)
v2 = ListNode(3)
v3 = ListNode(4)
head.next = v1
v1.next = v2
v2.next = v3
# 입력 만들어주기

cur = head

while cur and cur.next:
    cur.val, cur.next.val = cur.next.val, cur.val
    cur = cur.next.next

cur = head
while cur:
    print(cur.val)
    cur = cur.next


