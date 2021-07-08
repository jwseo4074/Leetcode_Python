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

"""
또 다른 풀이

root = prev = ListNode(None)
prev.next = head

while head and head.next :
    # b 가 a(head)를 가리키도록 할당
    b = head.next
    head.next = b.next
    b.next = head
    
    #prev 가 b 를 가리키도록 할당
    prev.next = b
    
    #다음번 비교를 위해 이동
    head = head.next
    prev = prev.next.next
return root.next

"""
