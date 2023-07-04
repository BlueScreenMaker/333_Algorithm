import heapq
import sys
INF=int(1e9)
T=int(sys.stdin.readline())


def dij(start):
    distance = [INF] * (n + 1)
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

for i in range(T):
    n,m,t=map(int,sys.stdin.readline().split())
    start, g,h=map(int,sys.stdin.readline().split())
    graph=[[] for i in range(n+1)]
    for j in range(m):
        a,b,c=map(int,sys.stdin.readline().split())
        graph[a].append([b,c])
        graph[b].append([a,c])
    site_proposed=[]
    for z in range(t):
        site_proposed.append(int(sys.stdin.readline()))
    point_s=dij(start)
    point_g=dij(g)
    point_h=dij(h)

    answer=[]
    for w in site_proposed:
        if point_s[g]+point_g[h]+point_h[w]==point_s[w] or point_s[h]+point_h[g]+point_g[w]==point_s[w]:
            answer.append(w)

    answer=sorted(answer)

    for z in answer:
        print(z,end=" ")
    print()
