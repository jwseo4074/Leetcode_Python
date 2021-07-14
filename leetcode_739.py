#temperatures = [55,38,53,81,61,93,97,32,43,78]
#
# cnt = 0
# list = []
# for i in range(0, len(temperatures)):
#     if  i == len(temperatures)-1:
#         list.append(0)
#     for j in range(i+1, len(temperatures)):
#         print("i = ", i, "j = ", j)
#         if i == len(temperatures)-2:
#             if temperatures[i] < temperatures[i+1]:
#                 list.append(1)
#             else :
#                 list.append(0)
#             break
#         elif temperatures[i]<temperatures[j]:
#             list.append(j-i)
#             break
#         elif j == len(temperatures)-1:
#             list.append(0)
#
# print(list)
# 무지성 브루트 포스

#정답
T = [55,38,53,81,61,93,97,32,43,78]

answer = [0] * len(T)
stack = []

for i, cur in enumerate(T):
    # 현재온도가 스택 값보다 높다면 정답 처리
    while stack and cur > T[stack[-1]]:
        last = stack.pop()
        answer[last] = i - last
    stack.append(i)

#return answer


# 예린이 정답
"""
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp = temperatures
        n = len(temp)
        trial = []
        ans = [0]*n

        for i in range(n-1):
            trial.append([i, temp[i]])
            while trial:
                if trial[-1][-1] < temp[i+1]:
                    index = trial.pop()[0]
                    ans[index] = i+1 - index
                else:
                    break
        
        return ans
    
"""