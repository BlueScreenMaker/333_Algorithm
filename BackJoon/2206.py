import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split(" "))

board = []
for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().rstrip())))

wall = []
for a in range(N):
    for b in range(M):
        if board[a][b] == 1:
            wall.append([a,b])

dx = [-1,1,0,0]
dy = [0,0,-1,1]
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
visited[0][0][0] = 1

def bfs(x,y,flag):
    que = deque()
    que.append([x,y,flag])
    while que:
        px, py, check = que.popleft()
        if px == N - 1 and py == M - 1:
            return visited[px][py][check]
        for i in range(4):
            nx = px + dx[i]
            ny = py + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if board[nx][ny] == 0 and visited[nx][ny][check] == 0:
                    visited[nx][ny][check] = visited[px][py][check] + 1
                    que.append([nx,ny,check])
                elif board[nx][ny] == 1 and check == 0:
                    visited[nx][ny][1] = visited[px][py][0] + 1
                    que.append([nx,ny,1])
    return -1

print(bfs(0,0,0))



'''
# 시간초과
def bfs(x,y, current_board, current_visited):
    que = deque()
    que.append([x,y])
    current_visited[x][y] = True
    count = 0
    while que:
        px,py = que.popleft()
        for i in range(4):
            nx = px + dx[i]
            ny = py + dy[i]
            if nx == N-1 and ny == M-1:
                return count
            elif 0 <= nx < N and 0 <= ny < M:
                if current_board[nx][ny] == 0 and not current_visited[nx][ny]:
                    que.append([nx,ny])
                    current_visited[nx][ny] = True
                    count += 1
    return -1

visited = [[False for _ in range(M)] for _ in range(N)]
origin = bfs(0,0,board, visited)

answer = []
if origin > 0:
    answer.append(origin)
for i in range(len(wall)):
    copy_board = copy.deepcopy(board)
    cx, cy = wall[i]
    copy_board[cx][cy] = 0
    visited = [[False for _ in range(M)] for _ in range(N)]
    result = bfs(0,0,copy_board, visited)
    if result > 0:
        answer.append(result)

if answer:
    print(min(answer))
else:
    print(-1)
'''