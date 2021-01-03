import sys
from collections import deque

R,C=map(int,sys.stdin.readline().split())

global Tforest
Tforest=[]

for t in range(0,R):
    string=sys.stdin.readline()
    Tforest.append(list(string))

visited=[[False for _ in range(0,C)] for _ in range(0,R)]

counting=[[0 for _ in range(0,C)] for _ in range(0,R)]


dx=[-1,1,0,0]
dy=[0,0,-1,1]

def escape(x,y,forest):
    que=deque()
    que.append((x,y))
    while que:
        x,y=que.popleft()
        for i in range(0,4):
            nx=x+dx[i]
            ny=y+dy[i]

            if nx<0 or ny<0 or nx>=R or ny>=C:
                continue

            if forest[nx][ny]=='D' and visited[nx][ny]==False: #비버굴 찾을 시 통과
                counting[nx][ny] += counting[x][y] + 1
                visited[nx][ny]=True
                return

            if forest[nx][ny]=='X' and visited[nx][ny]==False: #돌은 지나가지 못함
                visited[nx][ny]=False
                continue

            if forest[nx][ny]=='*' and visited[nx][ny]==False: #물도 못지나감
                visited[nx][ny]=True
                continue

            if forest[nx][ny]=='.' and visited[nx][ny]==False: #비어있는 이곳은 물이 찰까? => 검사가 필요
                visited[nx][ny] = True
                if Check_water(nx,ny,forest):
                    counting[nx][ny]+=counting[x][y]+1
                    que.append((nx,ny))


def Check_water(x,y,Tforest):
    water=False
    global Xp
    global Yp
    for z in range(0,4):
        p1 = x + dx[z]
        p2 = y + dy[z]
        if p1 < 0 or p2 < 0 or p1 >= R or p2 >= C:
            continue
        if Tforest[p1][p2]=='*':
            water=True
            Xp=p1
            Yp=p2
            break
    if water:
        for v in range(0,4):
            Xp= x+dx[v]
            Yp= y+dy[v]
            if Xp < 0 or Yp < 0 or Xp >= R or Yp >= C:
                continue
            if Tforest[Xp][Yp]=='.' and visited[Xp][Yp]==False:
                visited[Xp][Yp]=True
                Tforest[Xp][Yp]='*'
        return False
    else:
        return True



for a in range(0,R):
    for b in range(0,C):
        if Tforest[a][b]=='S':
            escape(a,b,Tforest)
        if Tforest[a][b]=='D':
            positionX=a
            positionY=b

if counting[positionX][positionY]>0:
    print(counting[positionX][positionY])
else:
    print("KAKTUS")