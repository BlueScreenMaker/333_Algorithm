def solution(m, n, puddles):
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for x, y in puddles:
        dp[y][x] = -1
    dp[1][1] = 1
    for i in range(1,n+1):
        for j in range(1,m+1):
            if dp[i][j] == -1:
                dp[i][j] = 0
                continue
            dp[i][j] += (dp[i-1][j] + dp[i][j-1]) % 1_000_000_007
    return dp[n][m]

print(solution(4,3,[[2, 2]]))