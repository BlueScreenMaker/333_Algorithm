import sys

from collections import deque

dx=[-1,1,0,0]
dy=[0,0,-1,1]
N,M,T=map(int,sys.stdin.readline().split())
castle=[]
for a in range(N):
    castle.append(list(map(int, sys.stdin.readline().split())))

visited=[[False for _ in range(0,M)] for _ in range(0,N)]



def Path(x,y):
    que=deque()
    que.append((x,y))
    gram = False
    while que:
        x,y=que.popleft()
        for i in range(0,4):
            nx=x+dx[i]
            ny=y+dy[i]
            if not gram:
                if nx<0 or ny<0 or nx>=N or ny>=M:
                    continue
                if castle[nx][ny]==1 and visited[nx][ny]==False:
                    visited[nx][ny]=True
                    continue
                if castle[nx][ny]==0 and visited[nx][ny]==False:
                    castle[nx][ny]=castle[x][y]+1
                    visited[nx][ny] = True
                    que.append((nx,ny))
                if castle[nx][ny]==2 and visited[nx][ny]==False:
                    gram=True
                    castle[nx][ny]=0
            elif gram:
                if nx<0 or ny<0 or nx>=N or ny>=M:
                    continue
                if visited[nx][ny]==False:
                    if castle[x][y]==1:
                        castle[nx][ny]+=castle[x][y]
                    else:
                        castle[nx][ny]=castle[x][y]+1
                    visited[nx][ny] = True
                    que.append((nx,ny))

    #         방문시......
    # 마법의 칼 만날 때도 생각해야해
    return castle[N-1][M-1]


value=Path(0,0)
if(value<=T):
    if(value==0):
        print("Fail")
    else:
        print(value)
else:
    print("Fail")


# print(castle)