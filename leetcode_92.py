#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# class Solution:
#     def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
left = 2
right = 4

head ,v1, v2, v3, v4 = ListNode(1), ListNode(2), ListNode(3), ListNode(4), ListNode(5)
head.next, v1.next, v2.next, v3.next = v1, v2, v3, v4
# 입력 만들어주기

if head is None or left == right:
    pass
    #return head

root = start = ListNode(None)
root.next = head

#start, end 지정
for _ in range(left-1):
    start = start.next
end = start.next

# 반복하면서 차례대로 노드 뒤집어주기
for _ in range(right-left):
    temp = start.next
    start.next = end.next
    end.next = end.next.next
    start.next.next = temp
# 이 부분 다시 해보면서 감 익히기

#return root.next
