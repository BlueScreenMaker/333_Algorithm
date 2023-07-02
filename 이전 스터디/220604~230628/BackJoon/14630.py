import heapq
import sys

INF=1e9
N=int(sys.stdin.readline())

num_list=[0]

for i in range(N):
    num_list.append(sys.stdin.readline().rstrip())

B, A = map(int,sys.stdin.readline().split())

relation=[[] for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(i+1, N+1):
        cost = 0
        for c1, c2 in zip(num_list[i], num_list[j]): # 리스트 요소들 묶기
            cost += (int(c1)-int(c2))**2
        relation[i].append([j, cost])
        relation[j].append([i, cost])

def Dijkstra():
    dist=[ INF for _ in range(N+1)]
    dist[B]=0
    que=[]
    heapq.heappush(que, [0, B])

    while que:
        cost, node=heapq.heappop(que)

        if dist[node]<cost:continue

        for next, count in relation[node]:
            total=count+cost
            if dist[next]>total:
                dist[next]=total
                heapq.heappush(que,[total,next])

    return dist[A]

print(Dijkstra())