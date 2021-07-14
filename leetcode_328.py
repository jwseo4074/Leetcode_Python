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
            # 초기 설정

            while odd and even and even.next:
                odd.next = odd.next.next
                # 처음 시작, 그 다음 홀수번째꺼로 포인터 조정

                if even.next.next:
                    even.next = even.next.next
                # 그 다음 짝수번째가 있을 때
                else:
                    even.next = None
                # 그 다음 짝수번째가 존재 하지 않을 때 => None 으로 할당

                odd = odd.next
                even = even.next
                # 그 다음 꺼로 각각 넘어가

            odd.next = root
            # while 문이 끝나고 난 후 root ( 짝수 시작이랑 홀수 끝이랑 연결 )

            return head
            # 답지에는 head.next 로 답을 내는 경우가 많은데 이게 더 직관적임

        else:
            return head