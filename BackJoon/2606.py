import sys
from collections import deque

def Check_virus(x):
    que=deque()
    que.popleft()
    visited[x]=True
    while que:
        if visited[x]==False:
            que.append(x)
            visited[x]=True

computer_num=int(sys.stdin.readline())
network_num=int(sys.stdin.readline())

visited=[False for _ in range(0,computer_num+1)]
worm_list=[[] for _ in range(0, computer_num + 1)]
for b in range(0,network_num):
    A,B=map(int,sys.stdin.readline().split())
    worm_list[A].append(B)

for i in range(0,len(worm_list)):
    for j in range(0,len(worm_list[i])):
        Check_virus(worm_list[i][j])
