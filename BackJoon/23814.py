import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split(" "))

board = []
for _ in range(N):
    board.append(list(sys.stdin.readline().rstrip()))

start_x, start_y = 0, 0
for a in range(N):
    for b in range(M):
        if board[a][b] == "S":
            start_x = a
            start_y = b
            break
print(f"start {start_x} {start_y}")
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [ [0 for _ in range(M)] for _ in range(N)]

def bfs(x, y):
    que = deque()
    que.append([x,y])
    visited[x][y] = 1
    count = 0
    while que:
        px, py = que.popleft()
        print(px, py)
        if count == 5:
            return visited[px][py]
        for i in range(4):
            nx = px + dx[i]
            ny = py + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if board[nx][ny] == "K" and visited[nx][ny] == 0:
                    count +=1
                    que.append([nx,ny])
                    visited[nx][ny] = visited[px][py] + 1
                elif board[nx][ny] == "." and visited[nx][ny] == 0:
                    que.append([nx, ny])
                    visited[nx][ny] = visited[px][py] + 1
    return -1

print(bfs(start_x, start_y))