# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is not None:
            odd = head
            even = head.next
            root = head.next

            while odd and even and even.next:
                odd.next = odd.next.next
                if even.next.next:
                    even.next = even.next.next
                else:
                    even.next = None
                odd = odd.next
                even = even.next
            odd.next = root

            return head
        else:
            return head