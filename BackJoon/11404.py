import sys

n=int(sys.stdin.readline())
m=int(sys.stdin.readline())

INF=int(1e9)

city=[[INF] * (n + 1) for _ in range(n + 1)]

for c in range(m):
    start,end,cost=map(int,sys.stdin.readline().split())
    city[start][end]=min(cost,city[start][end]) #왜 입력 받을때 최소값 비교함??? 이해안됨

for k in range(1, n + 1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i==j:
                city[i][j]=0
            else:
                city[i][j]=min(city[i][j], city[i][k] + city[k][j])

for w in range(1, n + 1):
    for v in range(1, n + 1):
        if city[w][v]==INF:
            print(0,end=" ")
        else:
            print(city[w][v], end=" ")
    print()


