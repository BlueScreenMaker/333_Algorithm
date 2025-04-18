import sys
n = int(sys.stdin.readline())

house = [[]]
for _ in range(n):
    house.append(list(map(int, sys.stdin.readline().split(" "))))

dp = [[0,0,0] for _ in range(n+1)]

INF = int(1e9)
answer = INF

for frist in range(3):
    # RGB 색 중 하나로 고정
    dp = [[INF for _ in range(3)] for _ in range(n+1)]
    dp[1][frist] = house[1][frist]

    for i in range(2, n+1):
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + house[i][0]
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + house[i][1]
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + house[i][2]
    
    for last in range(3):
        if last == frist:
            continue
        answer = min(answer, dp[n][last])

print(answer)