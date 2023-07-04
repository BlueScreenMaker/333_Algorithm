import sys

N=int(sys.stdin.readline())

time=[]
pay=[]
for x in range(N):
    t,p=map(int,sys.stdin.readline().split())
    time.append(t)
    pay.append(p)

dp=[0 for _ in range(N+1)]

flag=0
for i in range(0,N):
    flag=max(flag,dp[i]) # 이전에 최대값 소환
    if i+time[i]>N:
        continue
    dp[i+time[i]]=max(flag+pay[i], dp[i+time[i]])

print(max(dp))

