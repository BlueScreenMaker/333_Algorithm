import sys
from collections import deque

def bfs(start):
    que=deque()
    que.append(start)
    color[start]=1
    while que:
        check=que.popleft()
        for i in graph[check]:
            if color[check]==color[i]:
                return False
            if color[i]==0:
                color[i]=color[check]*-1
                que.append(i)
    return True

K=int(sys.stdin.readline())

for i in range(K):
    V,E=map(int,sys.stdin.readline().split())
    graph=[[] for _ in range(V+1)]
    color=[ 0 for _ in range(V+1)]
    flag=True
    for j in range(E):
        a,b=map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    for z in range(1,V+1):
        if color[z]==0:
            flag=bfs(z)
            if not flag: break

    if flag:
        print("YES")
    else:
        print("NO")