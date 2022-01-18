import sys

N,K=map(int,sys.stdin.readline().split())

coin_list=[]

for i in range(N):
    coin_list.append(int(sys.stdin.readline()))

dp=[0 for _ in range(K+1)]
dp[0]=1
for a in coin_list:
    for b in range(a,K+1):
        dp[b]+=dp[b-a]

print(dp[K])