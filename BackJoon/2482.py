import sys

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
mod = 1_000_000_003

dp = [ [0 for _ in range(K+1)] for _ in range(N+1)]

# idx = n번째 색상 선택한다.
# select = 지금 까지 고른 색상
for i in range(N+1):
    dp[i][1] = i
    dp[i][0] = 1

for idx in range(2, N + 1):
    for select in range(2, K + 1):
        dp[idx][select] = (dp[idx - 2][select - 1] + dp[idx - 1][select]) % mod

# 색상환은 원형
# 첫번째 색을 선택하면 마지막 색 선택 불가 > 첫번째색을 선택하면 양쪽의 색을 선택하지 못하기때문에 -3
print((dp[N-1][K] + dp[N-3][K-1])%mod)