def solution(sticker):
    length = len(sticker)
    if length == 1:
        return sticker[0]

    # 첫번째 스티커를 안뜯은 경우
    # i번째 스티커를 뜯는 경우 > sticker[i] + dp[i-2]
    # i번째 스티커를 뜯지 않는 경우 > dp[i-1]
    dp1 = [0] * length
    for i in range(1, length):
        dp1[i] = max(sticker[i] + dp1[i - 2], dp1[i - 1])

    # 첫번째 스티커를 뜯은 경우
    # 첫번째 스티커를 뜬는 경우 > dp[0] = sticker[0]
    dp2 = [0] * length
    dp2[0] = sticker[0]
    dp2[1] = dp2[0]
    for i in range(2, length - 1):
        dp2[i] = max(sticker[i] + dp2[i - 2], dp2[i - 1])

    return max(dp1[-1], dp2[-2])


print(solution([14, 6, 5, 11, 3, 9, 2, 10]))