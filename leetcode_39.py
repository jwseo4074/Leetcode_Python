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
