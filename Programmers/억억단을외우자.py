def solution(e, starts):
    answer = []

    multi = [0 for _ in range(e+1)]
    # step 1
    for i in range(1, e+1):
        for j in range(i, e+1):
            temp = i*j
            if temp > e:
                break
            if i == j:
                multi[temp] += 1
            else:
                multi[temp] += 2

    count = [0 for _ in range(e+1)]
    max_value = 0
    # step 2
    print(multi[7])
    for idx in range(e, 0, -1):
        if multi[idx] >= max_value:
            max_value = multi[idx]
            count[idx] = idx
        else:
            count[idx] = count[idx+1]

    for start in starts:
        answer.append(count[start])
    return answer

print(solution(8,[1,3,7]))