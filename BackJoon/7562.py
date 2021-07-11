import sys
from collections import deque

N=int(sys.stdin.readline())


def bfs(x, y):
    dx = [[-2, +2], [-1, +1]]
    dy = [[-1, +1], [-2, +2]]

    que = deque()

    que.append((x, y))


    while que:
        cx, cy = que.popleft()
        for i in range(2):
            for j in range(2):
                nx = cx + dx[i][j]
                for z in range(2):
                    ny = cy + dy[i][z]
                    if nx <= -1 or ny <= -1 or nx >= size or ny >= size:
                        continue
                    if nx == wantX and ny == wantY:
                        chess[nx][ny] = chess[cx][cy] + 1
                        break
                    if chess[nx][ny] == 0:
                        chess[nx][ny] = chess[cx][cy]+1
                        que.append((nx, ny))


for i in range(N):
    size=int(sys.stdin.readline())
    currentX,currentY=map(int,sys.stdin.readline().split())
    wantX,wantY=map(int,sys.stdin.readline().split())

    if currentX==wantX and currentY==wantY:
        print(0)
    else:
        chess=[[0 for i in range(size)] for i in range(size)]


        bfs(currentX, currentY)
        print(chess[wantX][wantY])



