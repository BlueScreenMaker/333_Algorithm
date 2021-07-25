from collections import deque

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(maps,visited,x,y,N,M):
    que=deque()
    que.append([x,y])
    visited[x][y]=True
    while que:
        positionX,positionY=que.popleft()
        for i in range(4):
            nx=positionX+dx[i]
            ny=positionY+dy[i]
            if ny<0 or nx<0 or nx>=N or ny>=M:
                continue
            if visited[nx][ny]==False:
                visited[nx][ny]=True
                que.append([nx,ny])
                maps[nx][ny]=maps[positionX][positionY]+1

def solution(maps):
    N=len(maps)
    M=len(maps[0])
    visited=[[False for _ in range(M)] for _ in range(N)]
    for a in range(N):
        for b in range(M):
            if maps[a][b]==0:
                visited[a][b]=True
    bfs(maps,visited,0,0,N,M)

    if maps[-1][-1]!=1:
        return maps[-1][-1]
    else:
        return -1


print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))