# class Solution:
#     def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

"""
k부터 출발해 모든 노드가 신호를 받을 수 있는 시간을 계산하라. 불가능할 경우 -1을 리턴한다.
입력값 (u,v,w) 는 각각 출발지, 도착지, 소요 시간으로 구성되며, 전체 노드의 개수는 N으로 입력받는다.
"""

# 정답코드

import collections
import heapq

times = [[2,1,1],[2,3,1],[3,4,1]]
n = 4
k = 2
# output = 2

graph = collections.defaultdict(list)

# 그래프 인접 리스트 구성
for u,v,w in times:
    graph[u].append((v,w))

# 큐 변수 : [(소요시간, 정점)]
Q = [(0, k)]
dist = collections.defaultdict(int)

# 우선순위 큐 최솟값 기준으로 정점까지 최단 경로 삽입
while Q:
    time, node = heapq.heappop(Q)
    print("time = ", time, "node = ", node)
    if node not in dist:
        dist[node] = time
        print("dist = ", dist)
        for v,w in graph[node]:
            alt = time + w
            heapq.heappush(Q, (alt,v))
            print("Q = ", Q)

# 모든 노드의 최단 경로 존재 여부 판별
if len(dist) == n:
    pass
    #return max(dist.values())
#return -1


