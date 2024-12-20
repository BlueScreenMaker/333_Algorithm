import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

dp = [ 1 for _ in range(N)]

for i in range(1, N):
    for j in range(0, i):

        # 왼 → 오 기준: 증가 수열
        if nums[i] > nums[j]:
            dp[i] = max(dp[i], dp[j]+1)

for i in range(1, N):
    for j in range(0, i):
        # 오 → 왼 기준: 증가 수열
        if nums[i] < nums[j]:
            dp[i] = max(dp[i], dp[j]+1)

# 왼 → 오 증가 수열과 오 → 왼 증가 수열을 합치다보면 어느순간 피크 지점이 생김
# 피크 지점 == 증가하다 감소하기 시작하는 지점
print(max(dp))