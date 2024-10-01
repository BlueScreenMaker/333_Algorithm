import sys
from collections import deque

N = int(sys.stdin.readline())

ocean = []
for _ in range(N):
    ocean.append(list(map(int, sys.stdin.readline().split())))

x_pos, y_pos = 0, 0
for a in range(N):
    for b in range(N):
        if ocean[a][b] == 9:
            x_pos = a
            y_pos = b
            ocean[a][b] = 0
            break

bady_size = 2

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def is_possible_eat(x, y, bady_size):
    visited = [[False for _ in range(N)] for _ in range(N)]
    distance = [[0 for _ in range(N)] for _ in range(N)]

    eats = []
    que = deque()
    que.append((x, y))
    visited[x][y] = True

    while que:
        cx, cy = que.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                if ocean[nx][ny] <= bady_size and not visited[nx][ny]:
                    visited[nx][ny] = True
                    que.append((nx, ny))
                    distance[nx][ny] = distance[cx][cy] + 1
                    if ocean[nx][ny] < bady_size and ocean[nx][ny] != 0 :
                        eats.append((nx, ny, distance[nx][ny]))

    return sorted(eats, key=lambda x:(x[2],x[0],x[1]))

move = 0
eat_count = 0
while True:
    candi = is_possible_eat(x_pos, y_pos, bady_size)

    if not candi:
        break

    check_x, check_y, dist = candi[0]
    move += dist
    eat_count += 1

    if bady_size == eat_count:
        bady_size += 1
        eat_count = 0

    ocean[x_pos][y_pos] = 0
    x_pos = check_x
    y_pos = check_y


print(move)


