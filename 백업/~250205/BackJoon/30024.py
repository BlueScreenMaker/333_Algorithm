import heapq
import sys

N, M = map(int, sys.stdin.readline().split(" "))
field = []
for _ in range(N):
    field.append(list(map(int, sys.stdin.readline().split(" "))))

K = int(sys.stdin.readline())

dx = [0,0,-1,1]
dy = [-1, 1, 0, 0]

visited = [[False for _ in range(M)] for _ in range(N)]

cons = []

for i in range(N):
    for j in range(M):
        if i==0 or i == N-1 or j ==0 or j==M-1:
            heapq.heappush(cons, (field[i][j], i, j))
            field[i][j] = 0

for a in range(K, 0, -1):
    check, cx, cy = heapq.heappop(cons)
    print(f"{cx+1} {cy+1}")
    if (cx < N-1 and field[cx+1][cy]):
        heapq.heappush(cons, (field[cx+1][cy], cx+1, cy))
        field[cx+1][cy] = 0
    if (cx > 0 and field[cx-1][cy]):
        heapq.heappush(cons, (field[cx-1][cy], cx-1, cy))
        field[cx-1][cy] = 0
    if (cy < M-1 and field[cx][cy+1]):
        heapq.heappush(cons, (field[cx][cy+1], cx, cy+1))
        field[cx][cy+1] = 0
    if (cy > 0 and field[cx][cy-1]):
        heapq.heappush(cons, (field[cx][cy-1], cx, cy-1))
        field[cx][cy-1] = 0
