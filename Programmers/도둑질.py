def solution(money):
    length = len(money)

    # 첫 지점 무조건 선택
    start_dp = [0 for _ in range(length)]
    start_dp[0] = money[0]
    start_dp[1] = max(money[0], money[1])
    for i in range(2, length-1): #마지막 집은 어짜피 못터니... 고려할 필요 없음
        start_dp[i] = max(start_dp[i-2]+money[i], start_dp[i-1])

    # 마지막 지점 무조건 선택
    end_dp = [0 for _ in range(length)]
    end_dp[0] = 0
    end_dp[1] = money[1]
    for i in range(2, len(money)):
        end_dp[i] = max(end_dp[i-2]+money[i], end_dp[i-1])

    return max(max(start_dp), max(end_dp))

print(solution([1, 2, 3, 1]))