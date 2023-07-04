import sys
N,M=map(int, sys.stdin.readline().split())

INF=int(1e9)
distance = [INF] * (N + 1)

graph=[]
for i in range(M):
    s,e,d=map(int,sys.stdin.readline().split())
    graph.append([s,e,d])


def bellman_ford(start):
    distance[start]=0
    for i in range(1,N+1):
        for j in range(M):
            begin, end, cost=graph[j][0],graph[j][1],graph[j][2]
            if distance[begin]!=INF and distance[end]>distance[begin]+cost:
                distance[end]=distance[begin]+cost
                if i==N:
                    return True
    return False


check_bellman=bellman_ford(1)

if check_bellman:
    print(-1)
else:
    for i in range(2,N+1):
        if distance[i]==INF:
            print(-1)
        else:
            print(distance[i])
