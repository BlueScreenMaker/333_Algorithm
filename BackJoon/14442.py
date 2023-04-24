import sys
from collections import deque

N,M,K = map(int, sys.stdin.readline().split())

board = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]

wall = []

for i in range(N):
    for j in range(M):
        if board[i][j] == "1":
            wall.append([i,j])
            
dx = [-1,1,0,0]
dy = [0,0,-1,1]
visited = [[[0]*(K+1) for _ in range(M)] for _ in range(N)]

que = deque()
def bfs():
    que.append([0,0,K])
    visited[0][0][K] = 1

    while que:
        px, py,break_cnt = que.popleft()
        if px == N-1 and py == M-1:
            print(visited)
            return visited[px][py][break_cnt]
        for i in range(4):
            nx = px + dx[i]
            ny = py + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            if board[nx][ny] == 1 and break_cnt > 0 and visited[nx][ny][break_cnt-1] == 0:
                visited[nx][ny][break_cnt-1] = visited[nx][ny][break_cnt] + 1
                que.append([nx,ny,break_cnt-1])
            elif board[nx][ny] == 0 and visited[nx][ny][break_cnt] == 0:
                visited[nx][ny][break_cnt] = visited[nx][ny][break_cnt] + 1
                que.append([nx,ny,break_cnt])
    return -1

print(bfs())