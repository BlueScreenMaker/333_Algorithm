def solution(sequence):
    answer = 0
    length = len(sequence)

    if length == 1:
        return max(sequence[0] * -1, sequence[0])
    else:
        dp = [[0, 0] for _ in range(length)]
        # # 1, -1, 1, -1 ..
        for i in range(1, length, 2):
            sequence[i] *= -1
        dp[0][0] = sequence[0]
        for j in range(1, length):
            dp[j][0] = max(sequence[j], dp[j - 1][0] + sequence[j])

        # -1, 1, -1, 1
        # 펄스 사용할 건데 이미 1이 들어갈 자리에 -1이 곱해진 상황 > 전체 배열에 -1을 곱한다

        for k in range(length):
            sequence[k] *= -1
        dp[0][1] = sequence[0]
        for h in range(1, length):
            dp[h][1] = max(sequence[h], dp[h - 1][1] + sequence[h])

    answer = max(map(max, dp))

    return answer