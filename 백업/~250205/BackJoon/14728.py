import sys

N, T = map(int, sys.stdin.readline().split(" "))

info = [[0,0]]
for _ in range(N):
    K, S = map(int, sys.stdin.readline().split(" "))
    info.append([K, S])


dp = [[0 for _ in range(T+1)] for _ in range(N+1)]

for i in range(1, N+1):
    time, score = info[i]
    for j in range(1, T+1):
        if j - time >= 0:
            dp[i][j] = max(dp[i][j], dp[i-1][j-time]+score, dp[i-1][j])
        dp[i][j] = max(dp[i][j], dp[i-1][j])

print(dp[N][T])