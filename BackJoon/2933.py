import sys
from collections import deque

R,C=map(int,sys.stdin.readline().split())

cave=[]
for a in range(R):
    string = sys.stdin.readline()
    cave.append(list(string))


throw_number=int(sys.stdin.readline())
throw_high=list(map(int, sys.stdin.readline().split()))

visited = [[False for _ in range(0,C)] for _ in range(0,R)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def reset(v):
    for i in range(0,R):
        for j in range(0,C):
            v[i][j]==False

global cluster
cluster=[]


def check_cluster(x,y):
    que=deque()
    que.append((x,y))
    cluster.clear()
    visited[x][y]=True
    while que:
        x,y=que.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or ny<0 or nx>=C or ny>=R:
                continue
            if cave[nx][ny]=='.' and visited[nx][ny]==False:
                continue
            if cave[nx][ny]=='x' and visited[nx][ny]==False:
                if nx==R-1:
                    return -1
                else:
                    cluster.append([nx,ny])
                    print(cluster)
                    visited[nx][ny]=True
                    que.append((nx,ny))

    return 0

def fall_cluster(cluster):
    for i in range(len(cluster),0,-1):
        Xpoint=cluster[i][0]
        Ypoint=cluster[i][1]
        for i in range(Xpoint+1,R):
            if cluster[Xpoint+1][Ypoint]=='.':
                cluster[Xpoint][Ypoint] = '.'
                cluster[Xpoint+1][Ypoint]='x'


for i in range(0,len(throw_high)):
    global high
    high = R - throw_high[i]
    if i%2==1:
        for j in range(0,C):
            if cave[high][j]=='x':
                cave[high][j]='.'
                for a in range(0,R):
                    for b in range(0,C):
                        if cave[a][b]=='x':
                            check_cluster(a,b)
                if check!=0:
                    reset(visited)
                    continue
                else:
                    fall_cluster(cluster)
                    reset(visited)

                break
    else:
        for j in range(C,0,-1):
            if cave[high][j]=='x':
                cave[high][j]='.'
                check = check_cluster(high, j)
                if check != 0:
                    reset(visited)
                    continue
                else:
                    fall_cluster(cluster)
                    reset(visited)

                break


for a in range(0, R):
    for b in range(0, C):
        print(cave[a][b], end='')
    print()