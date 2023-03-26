import sys
import copy
from collections import deque

chess = []
for a in range(8):
    chess.append(list(sys.stdin.readline().rstrip()))

visited = [[False for _ in range(8)] for _ in range(8)]

# 벽 위치 파악
wall = []
for x in range(8):
    for y in range(8):
        if chess[x][y] == "#":
            wall.append([x, y])

dx = [0, -1, 1, 0, 0, 1, 1,-1,-1]
dy = [0, 0, 0, -1, 1, -1, 1, 1, -1]


# 벽 내리기
def down_wall():
    temp_map = copy.deepcopy(wall)
    for i in range(0, 7):
        for j in range(0,7):
            if temp_map[i][j] == "#":
                temp_map[i+1][j] == "#"
# 위 아래 좌 우
def bfs(start_x, start_y):
    que = deque()
    que.append([start_x, start_y])
    visited[start_x][start_y] = True
    while que:
        px, py = que.popleft()
        if px == 0 and py == 7:
            return True
        else:
            possible = []
            for i in range(4):
                nx = px + dx[i]
                ny = py + dy[i]
                if nx < 0 or ny < 0 or nx >= 8 or ny >= 8:
                    continue
                if not visited[nx][ny] and chess[nx][ny] == ".":
                    if [nx, ny] in wall:
                        possible.append(False)
                    else:
                        possible.append(True)
                        visited[nx][ny] = True
                        que.append([nx,ny])
            down_wall()
            if not all(possible):
                return False
    return False

if bfs(7,0):
    print(1)
else:
    print(0)

