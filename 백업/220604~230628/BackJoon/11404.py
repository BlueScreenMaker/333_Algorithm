import sys

n=int(sys.stdin.readline())
m=int(sys.stdin.readline())

INF=int(1e9)

city=[[INF] * (n + 1) for _ in range(n + 1)]

for c in range(m):
    start,end,cost=map(int,sys.stdin.readline().split())
    city[start][end]=min(cost,city[start][end]) # 1 → 4 비용 2 와 1 → 4 비용 3이 있어서 최솟값 비교

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


