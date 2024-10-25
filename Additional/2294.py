import sys

N, K = map(int, sys.stdin.readline().split())
coins = []
for _ in range(N):
    coins.append(int(sys.stdin.readline()))

dp = [(1e9) for _ in range(K+1)]
dp[0] = 0

for coin in coins:
    for i in range(coin, K+1):
        dp[i] = min(dp[i], dp[i-coin]+1)

if dp[K] == 1e9:
    print(-1)
else:
    print(dp[K])