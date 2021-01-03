import sys

from collections import deque

dx=[-1,1,0,0]
dy=[0,0,-1,1]
N,M,T=map(int,sys.stdin.readline().split())
castle=[]
for a in range(N):
    castle.append(list(map(int, sys.stdin.readline().split())))

visited=[[False for _ in range(0,M)] for _ in range(0,N)]

castle_gram=[[ 0 for _ in range(0,M)] for _ in range(0,N)]

answer=10001


def Path(x,y,point):
    que=deque()
    que.append((x,y,point))
    global answer
    while que:
        x,y,point=que.popleft()
        visited[x][y]=True
        if x==N-1 and y==M-1:
            answer=min(answer,point)
        for i in range(0,4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or ny<0 or nx>=N or ny>=M:
                continue
            if castle[nx][ny]==1 and visited[nx][ny]==False:
                visited[nx][ny]=True
                continue
            if castle[nx][ny]==0 and visited[nx][ny]==False:
                visited[nx][ny] = True
                que.append((nx,ny,point+1))
            if castle[nx][ny]==2 and visited[nx][ny]==False:
                castle[nx][ny]=0
                visited[nx][ny]=True
                answer=min(answer,N-nx+M-ny+point-1)

    return answer


value=Path(0,0,0)

if(value<=T):
    print(value)
else:
    print("Fail")

