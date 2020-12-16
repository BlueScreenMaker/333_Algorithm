import sys
from collections import deque


def Check_virus(graph, start, visited, count):
    que=deque([start])
    visited[start]=True

    while que:
        check=que.popleft();
        for i in graph[check]:
            if not visited[i]:
                que.append(i)
                count += 1
                visited[i]=True
    return count

computer_num=int(sys.stdin.readline())
network_num=int(sys.stdin.readline())

visited=[False]*(computer_num+1)

worm_list=[[] for _ in range(0, computer_num + 1)]

for b in range(0,network_num):
    A,B=map(int,sys.stdin.readline().split())
    worm_list[A].append(B)

print(Check_virus(worm_list,1,visited,0))