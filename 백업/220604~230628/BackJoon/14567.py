import sys

N,M=map(int,sys.stdin.readline().split(" "))

prerequisite=[[] for _ in range(N+1)]

for x in range(M):
    A,B=map(int,sys.stdin.readline().split(" "))
    prerequisite[B].append(A)

dp=[ 0 for _ in range(N+1)]

for y in range(1,N+1):
    if not prerequisite[y]:
        dp[y]=1

for i in range(1,N+1):
    if prerequisite[i]:
        for check in prerequisite[i]:
            dp[i]=max(dp[check]+1, dp[i])

print(' '.join(map(str, dp[1:])))