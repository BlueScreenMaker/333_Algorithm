import sys

N, M = map(int, sys.stdin.readline().split(" "))

MAX = int(1e9)
distance = [[MAX for _ in range(N+1)] for _ in range(N+1)]

height = [[] for _ in range(N+1)]
for _ in range(M):
    a, b= map(int, sys.stdin.readline().split(" "))
    distance[a][b] = 1

for k in range(1, N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            distance[i][j] = min(distance[i][j], distance[i][k]+distance[k][j])

answer = 0
for a in range(1,N+1):
    temp = 0
    for b in range(1, N+1):
        if distance[a][b] != MAX or distance[b][a] != MAX:
            temp += 1
    if temp == N-1:
        answer += 1

print(answer)