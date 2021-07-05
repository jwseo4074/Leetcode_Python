import collections

strs = ["eat","tea","tan","ate","nat","bat"]
dic = collections.defaultdict(list)

# 기본 디폴트 값으로 list 를 넣어주겠다 !!
# 매우 중요
# print(dic)

for s in strs:
    dic[''.join(sorted(s))].append(s)
print(list(dic.values()))


"""
올린 정답

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        #import collections

        #strs = ["eat","tea","tan","ate","nat","bat"]
        dic = collections.defaultdict(list)

        # 기본 디폴트 값으로 list 를 넣어주겠다 !!
        # 매우 중요
        # print(dic)

        for s in strs:
            dic[''.join(sorted(s))].append(s)
        return list(dic.values())

"""