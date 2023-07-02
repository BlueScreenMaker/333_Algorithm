import sys
from collections import deque

N,M=map(int, sys.stdin.readline().split(' '))

info=[]
visitied=[[ False for _ in range(M)] for _ in range(N)]
for i in range(N):
    temp=sys.stdin.readline().strip()
    info.append(list(temp))

startX, startY=0,0
for a in range(N):
    for b in range(M):
        if info[a][b]=='0':
            startX=a
            startY=b

dx=[-1,1,0,0]
dy=[0,0,-1,1]

key_list=[]
dist=[[0 for _ in range(M)] for _ in range(N)]
def searching(x,y):
    que=deque()
    que.append([x,y])
    dist[x][y]=1
    while que:
        px,py=que.popleft()
        for j in range(4):
            nx=px+dx[j]
            ny=py+dy[j]
            if nx<0 or ny<0 or nx>=N or ny>=M: continue
            if info[nx][ny]=='1':
                return dist
            else:
                print(nx,ny)
                if not info[nx][ny]=='#':
                    if info[nx][ny]=='a' or 'b' or 'c' or 'd' or 'e' or 'f':
                        key_list.append(info[nx][ny])
                        dist[nx][ny]+=dist[px][py]
                        info[nx][ny]='.'
                        que.append([nx,ny])
                    elif info[nx][ny]=='A' or 'B' or 'C' or 'D' or 'E' or 'F':
                        if info[nx][ny].lower() in key_list:
                            dist[nx][ny] += dist[px][py]
                            info[nx][ny] = '.'
                            que.append([nx,ny])

                    else:
                        dist[nx][ny] += dist[px][py]
                        que.append([nx,ny])


print(searching(startX,startY))