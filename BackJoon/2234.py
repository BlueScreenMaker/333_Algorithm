import sys
from collections import deque

dx=[0,0,-1,1]
dy=[-1,1,0,0] #왼쪽 오른쪽 위 아래

# 1=서쪽(왼쪽) 2=북쪽(위) 4=동쪽(오른쪽) 8=남쪽(아래)


def bfs(x,y):
    que=deque()
    que.append([x,y])
    visited[x][y]=True
    count=1
    while que:
        px,py=que.popleft()
        for i in range(4):
            nx=px+dx[i]
            ny=py+dy[i]
            if nx<0 or ny<0 or nx>=M or ny>=N: continue
            if not visited[nx][ny]:
                if i==0:
                    if 1&info[nx][ny]: continue # 1 = 001 이고 만약 5인경우 5=101 and 연산을 취하면 1부분에서 1이 생겨 만족
                elif i==1:
                    if 4&info[nx][ny]:continue
                elif i==2:
                    if 2&info[nx][ny]:continue
                elif i==3:
                    if 8&info[nx][ny]:continue
                que.append([nx,ny])
                visited[nx][ny]=True
                count+=1

    return count


N,M=map(int,sys.stdin.readline().split())

info=[]
for i in range(M):
    info.append(list(map(int,sys.stdin.readline().split())))

visited=[[False for _ in range (N)] for _ in range(M)]

total_room=0
max_size=0

for a in range(M):
    for b in range(N):
        if not visited[a][b]:
            total_room += 1
            max_size=max(max_size,bfs(a,b))


print(total_room)
print(max_size)