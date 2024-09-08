import sys

N = int(sys.stdin.readline())

dp = [0 for _ in range(N+1)]

for i in range(1,N+1):
    time, count, *precede = map(int, sys.stdin.readline().split())
    dp[i] = time
    for check in precede:
        dp[i] = max(dp[i], dp[check]+time)

print(max(dp))