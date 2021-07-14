# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# #class Solution:
# #    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
#
# l1 = ListNode(1)
# next_node1 = ListNode(2)
# l1.next = next_node1
# next_node11 = ListNode(4)
# next_node1.next = next_node11
#
# l2 = ListNode(1)
# next_node2 = ListNode(3)
# l2.next = next_node2
# next_node22 = ListNode(4)
# next_node2.next = next_node22


# if (not l1) or (l2 and l1.val > l2.val):
#     l1, l2 = l2, l1
#
# if l1:
#     l1.next = self.mergeTwoLists(l1.next, l2)
# #return l1

# 파이썬 변수 스왑
"""
l1, l2 = l2, l1
=> 
temp = l1
l1 = l2
l2 = temp
"""