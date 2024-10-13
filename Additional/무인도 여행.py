from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]
def island(maps, x, y):
    que = deque()
    que.append([x,y])
    visited[x][y] = True
    total = int(maps[x][y])
    while que:
        cx, cy = que.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < row and 0 <= ny <column:
                if not visited[nx][ny]:
                    if maps[nx][ny] != "X":
                        que.append([nx,ny])
                        total += int(maps[nx][ny])
                        visited[nx][ny] = True
    return total


def solution(maps):
    answer = []
    global row
    row = len(maps)
    global column
    column = len(maps[0])
    global visited
    visited = [[False] * column for _ in range(row)]

    for i in range(row):
        for j in range(column):
            if maps[i][j] != "X" and not visited[i][j]:
                check = island(maps, i, j)
                answer.append(check)
    if answer:
        answer.sort()
        return answer
    else:
        return -1


print(solution(["X591X","X1X5X","X231X", "1XXX1"]))