import sys

N = int(sys.stdin.readline())

dp = [1 for _ in range(N+1)]

children = [0]
for i in range(N):
    children.append(int(sys.stdin.readline()))

for i in range(1, N+1):
    for j in range(1, i):
        if children[i] > children[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(N-max(dp))