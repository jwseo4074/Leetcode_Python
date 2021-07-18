# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
# 가장 많이 등장하는거 순서대로 k개
import collections

nums = [1,1,1,2,2,3]
k = 2

freqs = collections.Counter(nums)
#print(freqs)
# 카운터 함수 잘 이해해두기

# 파이썬다운 정답
print(list(zip(*collections.Counter(nums).most_common(k)))[0])
# return(list(zip(*collections.Counter(nums).most_common(k)))[0])

# 파이썬의 2가지 기능 = zip 과 * , collection 파일에서 다시 소개