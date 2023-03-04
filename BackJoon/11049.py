import sys

N = int(sys.stdin.readline())
array_info = []
for i in range(N):
    r, c = map(int, sys.stdin.readline().split(" "))
    array_info.append([r,c])

dp = [[0 for _ in range(N)] for i in range(N)]
# dp[i][j]: i ~ j 까지 행렬 곱셈 최소 값
for i in range(1, N): #몇 번째 대각선?
    for j in range(0, N-i): #대각선에서 몇 번째 열?
        if i == 1: #차이가 1밖에 나지 않는 칸
            dp[j][j+i] = array_info[j][0] * array_info[j][1] * array_info[j+i][1]
            continue
        
        dp[j][j+i] = 2**32 #최댓값을 미리 넣어줌
        for k in range(j, j+i): 
            dp[j][j+i] = min(dp[j][j+i], 
                             dp[j][k] + dp[k+1][j+i] + array_info[j][0] * array_info[k][1] * array_info[j+i][1])
                
    
print(dp[0][-1]) #맨 오른쪽 위