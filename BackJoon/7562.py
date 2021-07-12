import sys
from collections import deque

N=int(sys.stdin.readline())


def bfs(x, y):
    dx = [[-2, +2], [-1, +1]]
    dy = [[-1, +1], [-2, +2]]
    '''
    dx=[-2,-2,+2,+2,-1,+1,-1,+1]
    dy=[-1,+1,-1,+1,-2,-2,+2,+2]
    '''

    que = deque()
    que.append((x, y))

    while que:
        cx, cy = que.popleft()
        if cx==wantX and cy==wantY: #이미 cx,cy선에서 원하는 위치에 도달했을 수 있음
            break
        for i in range(2):
            for j in range(2):
                nx = cx + dx[i][j]
                for z in range(2):
                    ny = cy + dy[i][z]
                    if nx <= -1 or ny <= -1 or nx >= size or ny >= size:
                        continue
                    if chess[nx][ny] == 0:
                        chess[nx][ny] = chess[cx][cy]+1
                        que.append((nx, ny))



for i in range(N):
    size=int(sys.stdin.readline())
    currentX,currentY=map(int,sys.stdin.readline().split())
    wantX,wantY=map(int,sys.stdin.readline().split())


    chess=[[0 for i in range(size)] for i in range(size)]


    bfs(currentX, currentY)
    print(chess[wantX][wantY])




