# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# class Solution:
#     def diameterOfBinaryTree(self, root: TreeNode) -> int:

# root = TreeNode(1)
# left = TreeNode(2)
# right = TreeNode(3)
# root.right = right
# root.left = left
#
# left1 = TreeNode(4)
# right1 = TreeNode(5)
# left.left = left1
# left.right = right1
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 정답코드
class Solution:
    longest = 0
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return -1

            #왼쪽 오른쪽 각 리프 노드까지 탐색

            left = dfs(node.left)
            right= dfs(node.right)

            #가장 긴 경로
            self.longest = max(self.longest, left + right + 2)

            #상태값
            return max(left, right) + 1
        dfs(root)

        return self.longest
