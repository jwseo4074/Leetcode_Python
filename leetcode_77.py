# class Solution:
#     def combine(self, n: int, k: int) -> List[List[int]]:

n = 4
k = 2
list = []
for i in range(1,n+1):
    list.append(i)

answer = []

def dfs(index, path):
    if len(path) == k:
        answer.append(path)
        return

    for i in range(index, n):
        dfs(i + 1, path + [list[i]])

dfs(0,[])
print(answer)
#return answer


# 책에 나온 정답
"""
results = []
def dfs(elements, start, k):
    if k == 0:
        results.append(elements[:])
        return
    # 자신 이전의 모든 값을 고정하여 재귀 호출
    for i in range(start, n + 1):
        elements.append(i)
        dfs(elements, i + 1, k - 1)
        elements.pop()
 
dfs([], 1, k)
#return results
"""

#이것도 마찬가지로 파이썬 모듈 사용가능 ( itertools )