import sys
from collections import deque
from itertools import combinations

N,M=map(int,sys.stdin.readline().split())

city=[]


for i in range(N):
    city.append(list(map(int, sys.stdin.readline().split())))

chicken=[]

for i in range(N):
    for j in range(N):
        if city[i][j]==2:
            chicken.append([i,j])

dx=[-1,1,0,0]
dy=[0,0,-1,1]
def checking(x,y):
    visited = [[False for _ in range(N)] for _ in range(N)]
    que=deque()
    que.append([x,y])
    visited[x][y]=True
    while que:
        px,py=que.popleft()
        for i in range(4):
            nx=px+dx[i]
            ny=py+dy[i]
            if nx<0 or ny<0 or nx>=N or ny>=N:
                continue
            if city[nx][ny]==2:
                result=abs(x-nx)+abs(y-ny)
                return result
            elif visited[nx][ny]==False:
                visited[nx][ny]=True
                que.append([nx,ny])
    return 0

number=len(chicken)
answer=0
min_answer = 101
if number==M:
    for q in range(N):
        for p in range(N):
            if city[q][p]==1:
                answer+=checking(q,p)

else:
    mid=0
    for candi in list(combinations(chicken, number-M)):
        for x, y in candi:
            city[x][y] = 0
        for a in range(N):
            for b in range(N):
                if city[a][b]==1:
                    mid+=checking(a,b)
        if min_answer>mid:
            min_answer=mid
        for x, y in candi:
            city[x][y] = 2

print(min_answer)
print(answer)


