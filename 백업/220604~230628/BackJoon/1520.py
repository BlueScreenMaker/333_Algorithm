import sys
from collections import deque

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y):
    que=deque()
    que.append([x,y])
    while que:
        px,py=que.popleft()
        for i in range(4):
            nx=px+dx[i]
            ny=py+dy[i]
            if nx<0 or ny<0 or nx>=M or ny>=N:
                continue
            if nx==M-1 and ny==N-1:
                dp[nx][ny]+=1
                break
            if dp[nx][ny]==0 and info_map[nx][ny]<info_map[px][py]:
                dp[nx][ny]+=dp[px][py]
                que.append([nx,ny])

M,N=map(int,sys.stdin.readline().split(" "))

info_map=[]
dp=[[0 for _ in range(N)] for _ in range(M)]
visited=[[False for _ in range(N)] for _ in range(M)]

for i in range(M):
    info_map.append(list(map(int,sys.stdin.readline().split(" "))))

visited[0][0]=True
bfs(0,0)
# print(dp)
print(dp[M-1][N-1])

