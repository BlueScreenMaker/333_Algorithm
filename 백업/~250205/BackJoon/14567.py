import sys
N, M = map(int, sys.stdin.readline().split(" "))

subjects = [[] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int, sys.stdin.readline().split(" "))
    subjects[b].append(a)

dp = [0 for _ in range(N+1)]

for i in range(1,N+1):
    if subjects[i]:
       for j in subjects[i]:
           dp[i] = max(dp[j]+1, dp[i])
    else:
        dp[i] = 1

print(' '.join(map(str, dp[1:])))