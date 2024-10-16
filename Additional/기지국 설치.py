import math

def solution(n, stations, w):
    answer = 0

    need_install = []

    for i in range(1, len(stations)):
        need_install.append((stations[i]-w-1) - (stations[i-1]+w))

    # 제일 처음
    need_install.append(stations[0] - w - 1)
    need_install.append(n - (stations[-1] + w))

    for check in need_install:
        if check <= 0:
            continue
        answer += math.ceil( check / ((w*2) + 1))

    return answer

print(solution(11,[4, 11], 1))