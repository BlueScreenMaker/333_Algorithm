import sys
from collections import deque

N,M = map(int, sys.stdin.readline().split())
board = []
for i in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))

# 기준 레벨 구하기
# 해당 레벨보다 낮게 움직일 것이라고 가정
def make_standard_level():
    start = -1
    end = 10 ** 9
    while start+1 < end:
        mid = (start+end) // 2
        if bfs(0,0,mid):
            end = mid
        else:
            start = mid
    return end

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(x,y,level):
    if board[x][y] > level:
        return False
    que = deque()
    visited = [[[False] * 2 for _ in range(M)] for _ in range(N)]
    # 0 = 점프 안함
    # 1 = 점프 함
    que.append([x,y,0])
    visited[x][y][0] = True
    while que:
        px, py, jump = que.popleft()

        if px == N-1 and py == M-1:
            return True

        for i in range(4):
            nx = px + dx[i]
            ny = py + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if board[nx][ny] <= level and not visited[nx][ny][jump]:
                    que.append([nx,ny,jump])
                    visited[nx][ny][jump] = True
                # 지나가야할 경로의 레벨이 기준레벨보다 큰데, 아직 점프를 사용하지 않았을 때...
                elif jump == 0:
                    next_nx = nx + dx[i]
                    next_ny = ny + dy[i]
                    if 0 <= next_nx < N and 0 <= next_ny < M and board[next_nx][next_ny] <= level and not visited[next_nx][next_ny][1]:
                        que.append([next_nx, next_ny, 1])
                        visited[next_nx][next_ny][1] = True
    return False

print(make_standard_level())