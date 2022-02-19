import sys

pill=[]

while True:
    count=int(sys.stdin.readline())
    if count==0:
        break
    else:
        pill.append(count)

for case in pill:
    dp=[[0 for _ in range(case+1)] for _ in range(case+1)]
    for x in range(case+1):
        dp[0][x]=1
    for i in range(1,case+1):
        for j in range(1,case+1):
            if(i<=j):
                dp[i][j]=dp[i-1][j]+dp[i][j-1]
    print(dp[i][j])
