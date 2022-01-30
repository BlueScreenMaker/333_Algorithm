import sys

N=int(sys.stdin.readline())

if N%2!=0:
    print(0)

else:
     # dp의 인덱스 = 가로길이가 i일때, 칸을 채우는 경우의 수
    dp=[ 0 for i in range(N+2)]
    dp[0]=1 # i=4이고, j=4일때, dp[i-j]가 0 이 되기 때문
    dp[2]=3
    for i in range(4,N+1,2):
        dp[i]+=dp[i-2]*3 #dp[2]
        # 2칸인 경우에 발생하는 경우의 수가 3 이라서 3곱함
        for j in range(4,N+1,2):
            dp[i]+=dp[i-j]*2

             # i=4 j=4 4-4=0 1*2=0
             # i=6 j=4 // dp[2] * 2
             # i=8 j=6

    print(dp[N])