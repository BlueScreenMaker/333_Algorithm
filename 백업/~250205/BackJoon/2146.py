import sys
from collections import deque

N = int(sys.stdin.readline())

island = []
for _ in range(N):
    island.append(list(map(int, sys.stdin.readline().split(" "))))

answer = int(1e9)

dx = [0,0,1,-1]
dy = [1,-1,0,0]
def check_island(count,x,y):
    que = deque()
    que.append([x,y])
    visited[x][y] = True
    island[x][y] = count
    while que:
        px, py = que.popleft()
        for a in range(4):
            nx = px + dx[a]
            ny = py + dy[a]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if island[nx][ny] == 1:
                    visited[nx][ny] = True
                    island[nx][ny] = count
                    que.append([nx,ny])

visited = [[False for _ in range(N)] for _ in range(N)]
count = 1
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            if island[i][j] == 1 and not visited[i][j]:
                check_island(count, i, j)
                count += 1

def bridge(point):
    global answer
    dist = [[-1 for _ in range(N)] for _ in range(N)]
    queue = deque()

    for i in range(N):
        for j in range(N):
            if island[i][j] == point:
                queue.append([i, j])
                dist[i][j] = 0

    while queue:
        xx, yy = queue.popleft()
        for a in range(4):
            cx = xx + dx[a]
            cy = yy + dy[a]
            if 0 <= cx < N and 0 <= cy < N:
                if island[cx][cy] > 0 and island[cx][cy] != point:
                    answer = min(answer, dist[xx][yy])
                    return
                if island[cx][cy] == 0 and dist[cx][cy] == -1:
                    dist[cx][cy] = dist[xx][yy] + 1
                    queue.append([cx, cy])

for start in range(1, count):
    bridge(start)

print(answer)