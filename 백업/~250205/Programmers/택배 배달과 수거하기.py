def solution(cap, n, deliveries, pickups):
    answer = 0

    d_sum = 0
    p_sum = 0
    for i in range(n-1, -1, -1):
        count = 0
        d_sum += deliveries[i]
        p_sum += pickups[i]
        while d_sum > 0 or p_sum > 0:
            d_sum -= cap
            p_sum -= cap
            count += 1
        answer += (i+1) * 2 * count

    return answer

print(solution(4,5,[1, 0, 3, 1, 2], 	[0, 3, 0, 4, 0]))