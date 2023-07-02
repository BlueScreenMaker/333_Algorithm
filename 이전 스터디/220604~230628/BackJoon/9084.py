import sys

case=int(sys.stdin.readline())

for i in range(case):
    coins_count=int(sys.stdin.readline())
    coins=list(map(int, sys.stdin.readline().split()))
    price=int(sys.stdin.readline())
    dp=[0 for _ in range(price+1)]
    dp[0]=1
    for coin in coins:
        for j in range(coin,price+1):
            dp[j]+=dp[j-coin]
    print(dp[price])

