import sys

N = int(sys.stdin.readline())
graph = [[int(1e9) for _ in range(N+1)] for _ in range(N+1)]
for i in range(N-1):
    a, b, c = map(int, sys.stdin.readline().split(" "))
    graph[a][b] = c
    graph[b][a] = c

for k in range(N):
    for i in range(N):
        for j in range(N):
            graph[i][j] = min(graph[i][j],graph[i][k] + graph[k][j])

print("\n".join(map(str, graph)))