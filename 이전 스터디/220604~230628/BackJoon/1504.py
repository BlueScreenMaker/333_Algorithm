import heapq
import sys

v,e=map(int, sys.stdin.readline().split())
INF=int(1e9)
graph=[[] for _ in range (v+1)]

for i in range(0,e):
    v1,v2,k=map(int, sys.stdin.readline().split())
    graph[v1].append([v2,k])

e1,e2=map(int,sys.stdin.readline().split())

def dij(start):
    distance = [INF] * (v + 1)
    que=[]
    heapq.heappush(que,[0,start])
    distance[start]=0
    while que:
        d,check=heapq.heappop(que)
        if distance[check]<d:
            continue
        for i in graph[check]:
            cost=d+i[1]
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(que,[cost,i[0]])
    return distance


one=dij(1)
two=dij(e1)
three=dij(e2)

path1=one[e1]+two[e2]+three[v]
path2=one[e2]+three[e1]+two[v]

ans=min(path1,path2)

if ans>=INF:
    print(-1)
else:
    print(ans)



