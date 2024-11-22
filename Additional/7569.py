import sys
from collections import deque

#가로 세로 높이
M, N, H = map(int, sys.stdin.readline().split(" "))

boxes = []
for _ in range(H):
    temp = []
    for _ in range(N):
        temp.append(list(map(int, sys.stdin.readline().split(" "))))
    boxes.append(temp)
# boxes[z][x][y]

que = deque()
visited = [[[False for _ in range(M)] for _ in range(N)] for _ in range(H)]
for z in range(H):
    for x in range(N):
        for y in range(M):
            # 익은 토마토의 위치를 일단 넣어줌
            if boxes[z][x][y] == 1 and not visited[z][x][y]:
                que.append([z, x, y])
                visited[z][x][y] = True


dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

while que:
    cz, cx, cy = que.popleft()
    for i in range(6):
        nz = cz + dz[i]
        nx = cx + dx[i]
        ny = cy + dy[i]
        if 0 <= nz < H and 0 <= nx < N and 0 <= ny < M:
            if boxes[nz][nx][ny] == 0 and not visited[nz][nx][ny]:
                que.append([nz, nx, ny])
                boxes[nz][nx][ny] = boxes[cz][cx][cy] + 1
                visited[nz][nx][ny] = True

day = 0
for z in range(H):
    for x in range(N):
        for y in range(M):
            if boxes[z][x][y] == 0:
                print(-1)
                exit()
            day = max(day, boxes[z][x][y])

print(day - 1)