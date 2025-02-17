import sys
import copy

N, M = map(int, sys.stdin.readline().split(" "))

board = []
for i in range(N):
    board.append(list(map(int, sys.stdin.readline().split(" "))))

dp = copy.deepcopy(board)

# 제일 첫 행 초기화 > 첫 행은 오른쪽으로 전진할 수 밖에 없음
# 왼쪽으로 오는 경우는 갔던 길 되돌아오는 경우라서 성립 X
for a in range(1, M):
    dp[0][a] += dp[0][a-1]

# 왼 오 갱신
for x in range(1, N):
    left = dp[x][:]
    right = dp[x][:]

    # 왼 > 오
    for j in range(M):
        # 첫 번째 값은 위에서 오는 경우 밖에 없음 (왼쪽으로 올 수 없음 제일 끝이니까)
        if j == 0:
            left[j] += dp[x - 1][j]
        else:
            # 위에서 내려온거 vs 왼쪽에서 온거
            left[j] += max(dp[x - 1][j], left[j - 1])

    for j in range(M-1, -1, -1):
        if j == M-1:
            right[j] += dp[x - 1][j]
        else:
            right[j] += max(dp[x - 1][j], right[j + 1])

    for y in range(M):
        dp[x][y] = max(left[y], right[y])

print(dp[N-1][M-1])

