import sys

N = int(sys.stdin.readline())
children = list(map(int, sys.stdin.readline().split(" ")))

dp = [0 for _ in range(N+1)]

max_increase = 0
for i in range(0,N):
    point = children[i]
    dp[point] = dp[point-1] + 1
    max_increase = max(dp[point], max_increase)

print(N-max_increase)