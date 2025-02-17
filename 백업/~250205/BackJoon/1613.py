import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

dist = [[int(1e9) for _ in range(N+1)] for _ in range(N+1)]
condition = [[] for _ in range(N+1)]
for _ in range(K):
    a, b = map(int, sys.stdin.readline().split())
    condition[a].append(b)
    dist[a][b] = 1


for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])


S = int(sys.stdin.readline())
for _ in range(S):
    a,b = map(int, sys.stdin.readline().split())
    if dist[a][b] == int(1e9) and dist[b][a] == int(1e9):
        print(0)
    else:
        if dist[a][b] != int(1e9):
            print(-1)
        else:
            print(1)