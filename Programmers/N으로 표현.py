def solution(N, number):
    answer = 0

    if N == number:
        return 1

    candi_list = [set() for _ in range(8)]
    for a, b in enumerate(candi_list, start=1):  # b = candi_list 요소
        b.add(int(str(N) * a))

    flag = False
    for x in range(1, 8):
        # x = 2 일때,
        for y in range(0, x):
            # y는 0 ~ 1
            for z in candi_list[y]:
                # y==0 인 경우
                # y==1 인 경우
                for w in candi_list[x - y - 1]:
                    # x - y - 1 == 2 - 0 - 1 = 1
                    # x - y - 1 == 2 - 1 - 1 = 0
                    #  3 = 2 + 1 // 3 = 1 + 2 => 다른 연산으로 취급됨
                    candi_list[x].add(z + w)
                    candi_list[x].add(z - w)
                    candi_list[x].add(z * w)
                    if w != 0:
                        candi_list[x].add(z // w)
        if number in candi_list[x]:
            answer = x + 1
            flag = True
            break
    if flag:
        return answer
    else:
        return -1

print(solution(5, 12))