import copy
import sys
from collections import deque
from itertools import combinations


N=int(sys.stdin.readline())
info=[]

for i in range(N):
    info.append(list(map(str, sys.stdin.readline().split())))

empty=[]
teacher=[]
student=[]

for i in range(N):
    for j in range(N):
        if info[i][j]=='X':
            empty.append([i,j])
        elif info[i][j]=='T':
            teacher.append([i,j])

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def searching():
    for x,y in teacher:
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            while True:
                if 0<=nx<N and 0<=ny<N:
                    if info[nx][ny]=='S': # 학생 발견
                        return False
                    if info[nx][ny]=='O':
                        break
                else:
                    break
                nx=nx+dx[i]
                ny=ny+dy[i]
    return True


flag=False
for candi in list(combinations(empty, 3)):
    for x, y in candi:
        info[x][y] = 'O'
    if searching():
        flag=True
        break
    for x, y in candi:
        info[x][y]=='X'

if flag:
    print("YES")
else:
    print("NO")