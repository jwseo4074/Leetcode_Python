# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# class Solution:
#     def invertTree(self, root: TreeNode) -> TreeNode:

root = TreeNode(4)
left = TreeNode(2)
right = TreeNode(7)
root.right = right
root.left = left

left1 = TreeNode(1)
right1 = TreeNode(3)
left.left = left1
left.right = right1

left2 = TreeNode(6)
right2 = TreeNode(9)
right.left = left2
right.right = right2

def dfs(cur):
    if cur.val is None:
        return

    print(cur.val)
    if cur.left:
        dfs(cur.left)
    if cur.right:
        dfs(cur.right)

list_node = [root]
while list_node:
    cur = list_node.pop(0)

    if cur :
        replacenode = cur.left
        cur.left = cur.right
        cur.right = replacenode

        list_node.append(cur.left)
        list_node.append(cur.right)

dfs(root)
# return root