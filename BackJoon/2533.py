import sys
N = int(sys.stdin.readline())
sys.setrecursionlimit(10**6)

node = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split(" "))
    node[a].append(b)
    node[b].append(a)

visited = [False for _ in range(N+1)]
dp= [[0,1] for _ in range(N+1)]

def dfs(s_n):
    visited[s_n] = True
    for check in node[s_n]:
        if not visited[check]:
            dfs(check)
            dp[s_n][0] += dp[check][1]
            dp[s_n][1] += min(dp[check][0], dp[check][1])

dfs(1)
print(min(dp[1][0], dp[1][1]))