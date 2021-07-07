# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        answer = []
        cur = head
        while cur is not None:
            answer.append(cur.val)
            cur = cur.next
        i = 0
        while len(answer)>1:
            # 1보다 큼 조건에 주의
            # 만약에 0보다 크다 해놓으면 길이가 1일때 어캄 -> 에러 남
            if answer.pop(0) != answer.pop():
                return False
        return True
# 데크 자료형을 쓰면 시간을 훨씬 줄일수 있다
# 데크는 양방향으로 접근 가능 pop(0) 이랑 pop()

"""
파이썬 문법 => 다중 할당
a, b = 1, 2
"""
