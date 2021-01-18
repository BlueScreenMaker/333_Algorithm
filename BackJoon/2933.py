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
print(visited)

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def check_cluster(x,y):
    que=deque()
    que.append((x,y))
    while que:
        x,y=que.popleft()
        visited[x][y]=True
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            count=ny
            if nx<0 or ny<0 or nx>=C or ny>=R:
                continue
            if cave[nx][ny]=='.' or visited[nx][ny]==False:
                continue
            if cave[nx][ny]=='x' or visited[nx][ny]==False:
                visited[nx][ny]=True
                que.append((nx,ny))

                count+=1
        if count<=R:
            print("공중에 떠있는 상태")


    return

for i in throw_high:
    for j in range(0,C):
        high=R-i
        if cave[high][j]=='x':
            cave[high][j]='.'
            check_cluster(high,j)
            break
