import sys
from collections import deque

INF = 1_000_000_001
N,M = map(int, sys.stdin.readline().split(" "))

relation = [[] for _ in range(N+1)]
for _ in range(M):
    A,B,W = map(int,sys.stdin.readline().split(" "))
    relation[A].append([B,W])
    relation[B].append([A,W])

start, end = map(int, sys.stdin.readline().split(" "))


result = []
def bfs(mid):
    que = deque()
    que.append(start)
    visited[start] = True
    while que:
        node = que.popleft()
        if node == end:
            return True

        for check, weight in relation[node]:
            if not visited[check] and mid <= weight:
                visited[check] = True
                que.append(check)

    return False

answer = 0
s, e = 0, INF

while s <= e:
    mid = (s+e) // 2
    visited = [False for _ in range(N+1)]
    if bfs(mid):
        answer = max(answer, mid)
        s = mid + 1
    else:
        e = mid - 1

print(answer)

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
