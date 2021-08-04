
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# class Solution:
#     def longestUnivaluePath(self, root: TreeNode) -> int:


root = TreeNode(5)
left = TreeNode(4)
right = TreeNode(5)
root.right = right
root.left = left

left1 = TreeNode(1)
right1 = TreeNode(1)
left.left = left1
left.right = right1

left2 = TreeNode(None)
right2 = TreeNode(5)
right.left = left2
right.right = right2


result = 0

def dfs(node):
    global result
    if node is None:
        return 0
    # 없는거까지 내려가면 리턴 0

    left = dfs(node.left)
    right = dfs(node.right)
    # 제일 말단(리프)까지 재귀로 타고 들어감

    # 리프노드 도착했을때부터 시작
    if node.left and node.left.val == node.val:
        # node 의 왼쪽 자식 노드가 존재하고, 그 자식 노드의 값과 현대 노드의 값이 같을 때
        left += 1
    else :
        left = 0

    if node.right and node.right.val == node.val:
        # node 의 오른쪽 자식 노드가 존재하고, 그 자식 노드의 값과 현대 노드의 값이 같을 때
        right += 1
    else :
        right = 0

    #왼쪽과 오른쪽 자식 노드 간 거리의 합 최댓값이 결과
    result = max(result, left + right)

    #자식 노드 상태값 중 큰 값 리턴
    return max(left, right)

dfs(root)
print(result)