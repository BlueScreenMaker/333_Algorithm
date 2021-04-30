import heapq
import sys

v,e=map(int, sys.stdin.readline().split())
start=int(sys.stdin.readline())

graph=[[] for _ in range (v+1)]

distance=[300001]*(v+1)
for i in range(0,e):
    v1,v2,k=map(int, sys.stdin.readline().split())
    graph[v1].append([v2,k])

def dij(start):
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
dij(start)

for i in range(1,v+1):
    if distance[i]==300001:
        print("INF")
    else:
        print(distance[i])