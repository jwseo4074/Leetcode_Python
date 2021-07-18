# class Solution:
#     def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
candidates = [2,3,6,7]
target = 7
result = []

def dfs(csum, index, path):
    if csum < 0 :
        return
    if csum == 0 :
        result.append(path)
        return
    for i in range(index, len(candidates)):
        dfs(csum-candidates[i], i, path+[candidates[i]])

dfs(target, 0, [])
#return result


# dfs 의 핵심
# 무조건 짚고 넘어가기 !
# 순열이면 ? 순서가 상관있음, 1,2,3 이나 3,2,1 이나 다름 !!
# dfs 에 i 대신 0을 넣으면 됨
# 처음부터 다 돌아야함
