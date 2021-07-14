# Definition for singly-linked list.

#class Solution:
#    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

#   1->4->5,
#   1->3->4,
#   2->6
#Output: [1,1,2,3,4,4,5,6]

import heapq
#heapq 모듈 사용

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#lists = [[1,4,5],[1,3,4],[2,6]]

x1 = ListNode(1)
x2 = ListNode(4)
x3 = ListNode(5)
x1.next = x2
x2.next = x3

y1 = ListNode(1)
y2 = ListNode(3)
y3 = ListNode(4)
y1.next = y2
y2.next = y3

z1 = ListNode(2)
z2 = ListNode(6)
z1.next = z2

lists = [x1, y1, z1]

data = []

if len(lists) == 0:
    print(None)
    #return None

if len(lists) == 1:
    #return lists[0]
    print(lists[0])

for lst in lists:
    if lst == None: continue

    data.append(lst.val)
    while lst.next:  # 노드가 끝날 때까지 탐색
        lst = lst.next
        data.append(lst.val)

lists = ListNode(None)
if len(data) == 0:
    print(None)
    #return None
data.sort()
#print(data)

for i in range(len(data)):
    if i == 0:
        lists.val = data[i]
        # 제일 처음에만 val 설정

    else:
        node = lists
        # node.next가 None 없을 때까지, 더 input할 엘리먼트가 없을 때까지
        while node.next:
            node = node.next
        node.next = ListNode(data[i])

#return lists
