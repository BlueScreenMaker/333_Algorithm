import sys

n, m = map(int, sys.stdin.readline().split(" "))

names = []
for _ in range(n):
    names.append(int(sys.stdin.readline()))

max_number = m*m*n
dp = [max_number for _ in range(n+1)]

dp[n-1] = 0 # 제일 마지막 줄은 앞으로 이름을 적을 기회가 있으므로 계산하지 않는다.

'''
조건
1. 새줄 쓰기
2. 이어쓰기 (공백 포함)
'''
def solution(index):
    if dp[index] < max_number:
        return dp[index]

    space = m - names[index]
    for i in range(index+1, n+1):
        if (i == n): # 이름 전부 순회 완
            dp[index] = 0
            break
        dp[index] = min(dp[index], space*space + solution(i))
        space -= names[i] + 1 # 1 = 공백
    return dp[index]

print(solution(0))