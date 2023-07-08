import sys
from collections import deque

sys.setrecursionlimit(10**9)

INF = 1_000_000_001
N,M = map(int, sys.stdin.readline().split(" "))

relation = [[] for _ in range(N+1)]
for _ in range(M):
    A,B,W = map(int,sys.stdin.readline().split(" "))
    relation[A].append([B,W])
    relation[B].append([A,W])

start, end = map(int, sys.stdin.readline().split(" "))

visited = [False for _ in range(N+1)]
result = []
def bfs(start, w, end):
    que = deque()
    que.append(start)
    temp = w
    while que:
        node = que.popleft()
        for check, weight in relation[node]:
            if check == end:
                result.append(temp)
                temp = INF
            if not visited[check]:
                que.append(check)
                visited[check] = True
                if temp > weight:
                    temp = weight
    return

bfs(start, INF, end)
print(result)
'''
메모리 초과
result = []
def dfs(node, end, min_count):
    if node == end:
        return result.append(min_count)
    for island, weight in relation[node]:
        # print(f"island: {island} / weight: {weight}")
        if not visited[island]:
            visited[island] = True
            dfs(island, end, weight if weight < min_count else min_count)
            visited[island] = False

visited[start] = True
dfs(start,end, INF)
print(max(result))
'''
