import sys
from collections import deque

dx=[-1,1,0,0]
dy=[0,0,-1,1]
N,M,T=map(int,sys.stdin.readline().split())
castle=[]
for a in range(N):
    castle.append(list(map(int, sys.stdin.readline().split())))

test_castle=[]
for i in range(0,N):
    for j in range(0,M):
        castle[i][j]==test_castle[i][j]
gram=False
def Path(x,y):
    que=deque()
    que.append((x,y))
    count=0
    while que:
        x,y=que.popleft()
        for i in range(0,4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or ny<0 or nx>=N or ny>=M:
                continue
            if castle[nx][ny]==1:
                continue
            if castle[nx][ny]==0:
                test_castle[nx][ny]=test_castle[x][y]+1
                que.append((nx,ny))
            if castle[nx][ny]==2:
                gram=True
    #         방문시......
    # 마법의 칼 만날 때도 생각해야해
    return





visited=[[False for _ in range(0,M)] for _ in range(0,N)]