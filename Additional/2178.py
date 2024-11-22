import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

board = []
for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().rstrip())))

visited = [[False for _ in range(M)] for _ in range(N)]

dx = [0,0,-1,1]
dy = [-1,1,0,0]

que = deque()

# x좌표, y좌표, count
que.append([0,0,0])
visited[0][0] = True
answer = 0
while que:
    cx,cy,c_count = que.popleft()
    if (cx, cy) == (N-1, M-1):
        answer = c_count
        break
    for i in range(4):
        nx = cx + dx[i]
        ny = cy + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if board[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                que.append([nx,ny, c_count+1])

print(answer + 1)





