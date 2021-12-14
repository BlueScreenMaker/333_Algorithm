import sys
from collections import deque
from itertools import combinations

N,M=map(int,sys.stdin.readline().split())

lab=[]
for i in range(N):
    lab.append(list(map(int,sys.stdin.readline().split())))

candidate=[]
empty=0
wall=[]
for a in range(N):
    for b in range(N):
        if lab[a][b]==2:
            candidate.append([a,b])
        elif lab[a][b]==1:
            wall.append([a,b])

dx=[-1,1,0,0]
dy=[0,0,-1,1]
def searching(c):
    que=deque()
    for cx,cy in c:
        que.append([cx,cy])
    global count
    count=0
    while que:
        px,py=que.popleft()
        for i in range(4):
            nx=px+dx[i]
            ny=py+dy[i]
            if nx<0 or ny<0 or nx>=N or ny>=N:
                continue
            if visited[nx][ny]==False:
                visited[nx][ny]=True
                que.append([nx,ny])
    count += 1




for candi in list(combinations(candidate, M)):
    visited=[[False for _ in range(N)] for _ in range(N)]
    for x, y in candi:
        lab[x][y]=-1
        visited[x][y]=True
    for wx,wy in wall:
        visited[wx][wy]=True
    print(searching(candi))
    for x, y in candi:
        lab[x][y]=2