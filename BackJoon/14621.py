import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split(" "))

gender = [0 for _ in range(N+1)]
temp = list(sys.stdin.readline().rstrip().split(" "))
for a in range(N):
    if temp[a] == "M":
        gender[a+1] = 0
    else:
        gender[a+1] = 1

relation = [[] for _ in range(N+1)]
for b in range(M):
    u, v, d = map(int, sys.stdin.readline().split(" "))
    relation[u].append([v,d])
    # relation[v].append([u,d])

dist = [int(1e9) for _ in range(N+1)]

def bfs(start):
    que = deque()
    que.append([start,0])
    total = 0
    while que:
        node, check = que.popleft()
        min_value = int(1e9)
        for temp in relation[node]:
            if gender[temp[0]] != gender[node]:
                min_value = min(min_value, temp[1])
            else:
                continue
        total += min_value
    return total

print(bfs(1))