import heapq
import sys

def dijkstra(start):
    que=[]
    heapq.heappush(que,(0,start))
    distance[start]=0
    while que:
        dist, node=heapq.heappop(que)
        if distance[node]<dist:
            continue
        for check in grap[node]:
            cost=dist+check[1]
            if cost<distance[check[0]]:
                distance[check[0]]=cost
                heapq.heappush(que,(cost,check[0]))

INF = int(1e9)
T=int(sys.stdin.readline())

for i in range(T):
    N,M=map(int, sys.stdin.readline().split())
    grap=[ [] for _ in range(N+1)]
    for j in range(M):
        a, b, c=map(int, sys.stdin.readline().split())
        grap[a].append([b, c])
        grap[b].append([a, c])
    K = int(sys.stdin.readline())
    friend=list(map(int, sys.stdin.readline().split()))
    total_dis = [0 for _ in range(N + 1)]
    for pos in friend:
        distance = [INF for _ in range(N + 1)]
        dijkstra(pos)
        for pos in range(1,N+1):
            total_dis[pos]+=distance[pos]
    min_num=min(total_dis[1:])
    print(total_dis.index(min_num))
