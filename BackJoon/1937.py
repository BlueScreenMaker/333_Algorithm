import sys

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def dfs(x,y):
    if distance[x][y]:
        return distance[x][y]
    distance[x][y]=1
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx<0 or ny<0 or nx>=N or ny>=N: continue
        if forest[x][y]<forest[nx][ny]:
            distance[x][y]=max(distance[x][y], dfs(nx,ny)+1)
    return distance[x][y]

N = int(sys.stdin.readline())
forest=[]
standard=[]
for i in range(N):
    forest.append(list(map(int,sys.stdin.readline().split(" "))))

answer=0
distance=[[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        answer=max(answer,dfs(i,j))

print(answer)