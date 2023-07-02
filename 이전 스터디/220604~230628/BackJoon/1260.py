import sys
from collections import deque

N,M,start=map(int,sys.stdin.readline().split())
graph=[[] for a in range(N+1)]
for i in range(M):
    a,b=map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
for j in graph:
    j.sort()
visited=[False]*(N+1)


def dfs(start, visited,graph):
    visited[start]=True
    print(start,end=' ')
    for q in graph[start]:
        if not visited[q]:
            dfs(q,visited,graph)


def bfs(start,visited,graph):
    que=deque([start])
    visited[start]=True
    while que:
        check=que.popleft()
        print(check,end=' ')
        for p in graph[check]:
            if not visited[p]:
                que.append(p)
                visited[p]=True


dfs(start,visited,graph)
visited=[False for a in range(N+1)]
print()
bfs(start,visited,graph)