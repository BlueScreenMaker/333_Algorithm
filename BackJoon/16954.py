import sys
from collections import deque

chess = []
for a in range(8):
    chess.append(list(sys.stdin.readline().rstrip()))

que = deque()
que.append([7,0])
visited = [[False for _ in range(8)] for _ in range(8)]
dx = [0, -1, 1, 0, 0, -1, -1,1, 1]
dy = [0, 0, 0, -1, 1, -1, 1, -1, 1]

# 벽 위치 파악
def move_wall():
    temp_chess = [["." for _ in range(8)]for _ in  range(8)]
    for i in range(7):
        for j in range(8):
            if chess[i][j] == "#":
                temp_chess[i+1][j] = "#"
    return temp_chess

# 턴 계산
def bfs():
    # 전 단계에서 가지고있던 경우의 수
    length = len(que)
    while length > 0:
        px, py = que.popleft()
        length -= 1

        if chess[px][py] == "#":
            continue

        visited[px][py] = True
        for i in range(9):
            nx = px + dx[i]
            ny = py + dy[i]
            if 0 <= nx < 8 and 0 <= ny < 8:
                if chess[nx][ny] == "." and not visited[nx][ny]:
                    que.append([nx,ny])

        # 제 자리를 선택할 경우
        que.append([px,py])


result = 1

for i in range(8):
    bfs()
    if not que:
        result = 0
        break
    chess = move_wall()

print(result)
