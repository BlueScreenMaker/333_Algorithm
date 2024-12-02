import sys

N, K = map(int, sys.stdin.readline().split())
items = [[0,0]]

for _ in range(N):
    W, V = map(int, sys.stdin.readline().split())
    items.append([W,V])

dp = [[0 for _ in range(K+1)] for _ in range(N+1)]

for i in range(N+1):
    weight, value = items[i]
    for j in range(1, K+1):
        if j - weight >= 0:
            dp[i][j] = max(dp[i][j], dp[i-1][j], dp[i-1][j-weight]+value)
        dp[i][j] = max(dp[i][j], dp[i-1][j])

print(dp[N][K])