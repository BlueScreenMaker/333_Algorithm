import sys

N = int(sys.stdin.readline())
town = [0]+list(map(int, sys.stdin.readline().split()))

relation = [[] for _ in range(N+1)]
for _ in range(N-1):
    a,b = map(int, sys.stdin.readline().split())
    relation[a].append(b)
    relation[b].append(a)

dp = [[0, town[i]] for i in range(N+1)]
visited = [False for _ in range(N+1)]

def dfs(point):
    visited[point] = True
    for check in relation[point]:
        if not visited[check]:
            dfs(check)
            dp[point][0] = max(dp[check][0], dp[check][1])
            dp[point][1] += dp[check][0]
