# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
#
# class Solution:
#     def maxDepth(self, root: TreeNode) -> int:

# 입력이 [3,9,20,null,null,15,7] 일때

"""
트리를 구조화 해보면 다음과 같다. ( bfs 로 순회 )

TreeNode{val: 3,
         left: TreeNode{val: 9,
                        left: None,
                        right: None},
        right: TreeNode{val: 20,
                        left: TreeNode{val: 15,
                                       left: None,
                                       right: None},
                       right: TreeNode{val: 7,
                                       left: None,
                                       right: None}}}    
"""
root = TreeNode(3)
left = TreeNode(9)
right = TreeNode(20)
root.right = right
root.left = left

left1 = TreeNode(None)
right1 = TreeNode(None)
left.left = left1
left.right = right1

left2 = TreeNode(15)
right2 = TreeNode(7)
right.left = left2
right.right = right2

# print(root.val)
# print(root.left.val)
# print(root.right.val)
#
# print(root.left.left.val)
# print(root.left.right.val)
# print(root.right.left.val)
# print(root.right.right.val)

if root is None:
    # 루트가 비어있으면 바로 리턴
    pass
    #return 0
queue = collections.deque([root])
depth = 0

while queue:
    depth += 1
    # 큐 연산 추출 노드의 자식 노드 삽입

    for _ in range(len(queue)):
        cur_root = queue.popleft()
        # cur_root 는 큐의 제일 왼쪽 꺼

        if cur_root.left:
            queue.append(cur_root.left)
        if cur_root.right:
            queue.append(cur_root.right)

print(depth)
# BFS 반복 횟수 => 깊이
#return depth

