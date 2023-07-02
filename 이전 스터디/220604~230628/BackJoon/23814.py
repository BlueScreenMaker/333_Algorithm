import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split(" "))

board = []
for _ in range(N):
    board.append(list(sys.stdin.readline().rstrip()))

dist = []
for a in range(N):
    for b in range(M):
        if board[a][b] == "S":
            dist.append((a,b))
            board[a][b] = "."
        elif board[a][b] == "K":
            dist.append((a,b))
            board[a][b] = "."

dx = [-1,1,0,0]
dy = [0,0,-1,1]

dist_len = len(dist)

# S에서 K 까지의 거리 구하기
def bfs(idx):
    start_x, start_y = dist[idx]
    visited = [[0 for _ in range(M)] for _ in range(N)]
    que = deque()
    que.append([start_x, start_y])
    while que:
        px,py = que.popleft()
        for i in range(4):
            nx = px + dx[i]
            ny = py + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and board[nx][ny] != "X" :
                visited[nx][ny] = visited[px][py] +1
                que.append([nx,ny])

    for j in range(dist_len):
        if j == idx: continue
        nx, ny = dist[j]
        if visited[nx][ny] == 0:
            total_dist[nx][ny] = INF
        else:
            total_dist[nx][ny] = visited[nx][ny]

INF = 1e9
total_dist = [[INF for _ in range(dist_len)] for _ in range(dist_len)]
answer = INF
dfs_visited = [False for _ in range(dist_len)]

for a in range(dist_len):
    bfs(a)

def dfs(current, total, depth):
    global answer
    # 최소비용 아님
    if answer <= total:
        return
    if depth == 5:
        answer = min(answer, total)
    for next in range(dist_len):
        if dfs_visited[next] or total_dist[current][next] >= INF: continue
        dfs_visited[next] = True
        dfs(next, total + total_dist[current][next], depth+1)
        dfs_visited[next] = False

dfs_visited[0] = True
dfs(0,0,0)

if answer == INF:
    print(-1)
else:
    print(answer)