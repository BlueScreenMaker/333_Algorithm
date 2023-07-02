from collections import deque
from itertools import permutations
import sys

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    q = deque()
    count = [[0]*w for _ in range(h)]
    q.append([x, y])
    count[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx< 0 or ny<0 or nx>=h or ny>=w: continue
            if room[nx][ny] != 'x' and not count[nx][ny]:
                count[nx][ny] = count[x][y] + 1
                q.append([nx, ny])
    return count

while True:
    w, h = map(int, sys.stdin.readline().split())

    if not w and not h:
        break

    room, dust = [], []
    for i in range(h):
        row = list(sys.stdin.readline().strip())
        room.append(row)
        for j, z in enumerate(row):
            if z == 'o':
                loc_x, loc_y = i, j
            elif z == '*':
                dust.append([i, j])

    clean, flag = [], 0

    result = bfs(loc_x, loc_y)
    for i, j in dust:
        if not result[i][j]:
            flag = 1
            break
        clean.append(result[i][j] - 1)

    if flag:
        print(-1)
        continue

    dist = [[0] * len(dust) for _ in range(len(dust))]

    for i in range(len(dust) - 1):
        result = bfs(dust[i][0], dust[i][1])
        for j in range(i+1, len(dust)):
            dist[i][j] = result[dust[j][0]][dust[j][1]] - 1
            dist[j][i] = dist[i][j]

    per = list(permutations([i for i in range(len(dist))]))

    ans = int(1e9)
    for i in per:
        check = 0
        check += clean[i[0]]
        pos = i[0]
        for j in range(1, len(i)):
            end = i[j]
            check += dist[pos][end]
            pos = end
        ans = min(ans, check)
    print(ans)