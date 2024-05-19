import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
field = []
for _ in range(N):
    field.append(list(map(int, sys.stdin.readline())))

K = int(sys.stdin.readline())

dp = [[0 for _ in range(M)] for _ in range(N)]

dx = [0,0,-1,1]
dy = [-1, 1, 0, 0]

visited = [[False for _ in range(M)] for _ in range(N)]
def bfs(x,y):
    que = deque()
    que.append([x,y])
    visited[x][y] = True
    while que:
        px, py = que.popleft()
        for i in range(4):
            nx, ny = px+dx[i], py+dy[i]
            if 0 <= nx < M and 0 <= ny < N and visited[nx][ny] == False:
                que.append([nx,ny])
                visited[nx][ny] = True