import sys
from collections import deque

row, column=map(int, sys.stdin.readline().split())

guide=[]

for i in range(row):
    guide.append(list(sys.stdin.readline().rstrip()))

dx=[-1,1,0,0]
dy=[0,0,-1,1]
def searching(currX,currY):
    q=deque()
    q.append([currX,currY])
    acc=[[0 for _ in range(column)] for _ in range(row)]
    acc[currX][currY]=1
    result=0
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<row and 0<=ny<column:
                if guide[nx][ny]=='L' and acc[nx][ny]==0:
                    acc[nx][ny]=acc[x][y]+1
                    result=max(result,acc[nx][ny])
                    q.append([nx,ny])

    return result-1

count=0
for i in range(row):
    for j in range(column):
        if guide[i][j]=='L':
            count=max(count,searching(i,j))

print(count)



