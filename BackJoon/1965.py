import sys

N=int(sys.stdin.readline())

box_size=list(map(int,sys.stdin.readline().split()))

dp=[ 0 for _ in range(N)]

for i in range(N):
    dp[i]=1
    for j in range(i):
        if box_size[i]>box_size[j]:
            dp[i]=max(dp[i],dp[j]+1)

print(max(dp))