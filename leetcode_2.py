# # Definition for singly-linked list.
# class ListNode:
#  def __init__(self, val=0, next=None):
#      self.val = val
#      self.next = next
# #class Solution:
# #    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
# #
# l1 = ListNode(2)
# next_node = ListNode(4)
# l1.next = next_node
# next_node1 = ListNode(3)
# next_node.next = next_node1
#
# l2 = ListNode(5)
# next_node2 = ListNode(6)
# l2.next = next_node2
# next_node3 = ListNode(4)
# next_node2.next = next_node3
# # 연결리스트 만들기 끝
#
# """
# 1. l1 이랑 l2 뒤집는다
# 2. str 로 바꿔준다
# 3. 더한다
# 4. 연결 리스트로 바꿔준다
# """

prev,cur  = None,l1
while cur :
    next, cur.next = cur.next, prev
    prev, cur = cur, next
start_l1 = prev

prev,cur  = None,l2
while cur :
    next, cur.next = cur.next, prev
    prev, cur = cur, next
start_l2 = prev

l1_str = ""
while start_l1:
    l1_str += str(start_l1.val)
    start_l1 = start_l1.next

l2_str = ""
while start_l2:
    l2_str += str(start_l2.val)
    start_l2 = start_l2.next

answer = str(int(l1_str) + int(l2_str))

prev = None
for s in answer:
    node = ListNode(s)
    node.next = prev
    prev = node
return node




