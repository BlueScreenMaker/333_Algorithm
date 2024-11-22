import sys

N = int(sys.stdin.readline())

mod = 10_007

dp = [[0 for _ in range(0, 10)] for _ in range(N+1)]

for i in range(0, 10):
    dp[1][i] = 1

for x in range(2, N+1):
    for y in range(0, 10):
        for z in range(y, 10):
            dp[x][y] += dp[x-1][z]
        dp[x][y] %= mod

print(sum(dp[N]) % mod)
