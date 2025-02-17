import sys

N = int(sys.stdin.readline())
customer = list(map(int, sys.stdin.readline().split()))
T = int(sys.stdin.readline())

prefix = [0 for _ in range(N+1)]
for a in range(1, N+1):
    prefix[a] = prefix[a-1] + customer[a-1]

dp = [[0 for i in range(N+1)] for _ in range(4)]

for i in range(1, 4):
    for j in range(T, N + 1):
        # i = 소형 기관차 수
        # j = 객실 수
        dp[i][j] = max(dp[i][j - 1], dp[i - 1][j - T] + prefix[j] - prefix[j - T])

print(dp[-1][-1])