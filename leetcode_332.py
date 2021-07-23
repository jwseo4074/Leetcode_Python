# class Solution:
#     def findItinerary(self, tickets: List[List[str]]) -> List[str]:
import collections

tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
str_len = len(tickets)
answer = []
tickets.sort()
def dfs(string):
    if len(answer) == str_len + 1:
        return
    # answer 의 길이가 5이면 리턴 ( 다 돌았다는 뜻 )

    if len(answer) == str_len:
        answer.append(string)

    for i in range(0, str_len):
        if tickets[i][0] == string:
            answer.append(string)
            dfs(tickets[i][1])
            return

for i in range(0, str_len):
    if tickets[i][0] == "JFK":
        answer.append("JFK")
        dfs(tickets[i][1])
        #return

#return answer
print(answer)

# 뎁스 초과 ..

# # 그래프 그리고 pop 으로 재귀 호출 하면서 모두 꺼내 결과에 추가한다.
#
# # 정답코드
# graph = collections.defaultdict(list)
# # 그래프 순서대로 구성
#
# for a, b in sorted(tickets):
#     graph[a].append(b)
#
# route = []
#
# def dfs(a):
#     # 첫번째 값을 읽어 어휘 순 방문
#     while graph[a]:
#         dfs(graph[a].pop(0))
#     route.append(a)
#
# dfs('JFK')
# # 다시 뒤집어 어휘 순 결과로
#
# return route[::-1]