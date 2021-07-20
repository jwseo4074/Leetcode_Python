# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:

nums = [0,-1,1]
answer = []

def dfs(index, path):
    if len(nums) == len(path):
        list1 = []
        for s in path:
            list1.append(int(s))
        answer.append(list1)
        return

    for i in range(index, len(nums)):
        for char in nums:
            char = str(char)
            #print("char = ", char)

            if char not in path:
                dfs(i + 1, path + [char])

dfs(0,[])
print(answer)
# return answer


# 순열 모듈 사용 가능 ( 파이썬 )
"""
def permute(self, nums: List[int]) -> List[List[int]]:
    return list(itertools.permutations(nums))
"""
