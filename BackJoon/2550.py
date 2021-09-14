import sys

N=int(sys.stdin.readline())

switch=list(map(int, sys.stdin.readline().split(" ")))
light=list(map(int, sys.stdin.readline().split(" ")))

relationship=[[] for _ in range(N+1)]


for i in range(N):
    relationship[switch[i]].append(i)

for i in range(N):
    relationship[light[i]].append(i)


dp=[ 0 for _ in range(N)]

dp[0]=1
for i in range(1,N):
    dp[i]=1
    flag = relationship[switch[i]][1]
    for j in range(0,i):
        if flag>relationship[switch[j]][1]:
            dp[i]=max(dp[i],dp[j]+1)


print(max(dp))
