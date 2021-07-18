import sys
from collections import deque

T=int(sys.stdin.readline())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y):
    que=deque()
    que.append([x,y])

    visited[x][y]=True

    while que:
        positionX, positionY=que.popleft();

        for i in range(4):
            nx=positionX+dx[i]
            ny=positionY+dy[i]

            if nx<0 or ny<0 or nx>=H or ny>=W:
                continue

            if visited[nx][ny]==False and field[nx][ny]=='#':
                que.append([nx,ny])
                visited[nx][ny]=True


for i in range(T):
    H,W=map(int,sys.stdin.readline().split())
    field=[]
    for j in range(H):
        field.append(list(input()))

    visited=[[False for _ in range (W)] for _ in range(H)]
    count=0
    for a in range(H):
        for b in range(W):
            if field[a][b]=='#' and  visited[a][b]==False:
                bfs(a,b)
                count+=1
            else:
                continue
    print(count)