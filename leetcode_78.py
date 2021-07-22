# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:

nums = [1,2,3]
answer = []

def dfs(index, path):
    answer.append(path)

    for i in range(index, len(nums)):
        dfs(i + 1, path + [nums[i]])

dfs(0,[])
print(answer)