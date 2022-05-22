from itertools import combinations_with_replacement
from collections import Counter

def solution(n, info):
    max_diff, max_comb_cnt = 0, {}

    for comb in combinations_with_replacement(range(11), n):
        # comb = 총길이 n개, 어느 점수 과녁에 화살을 넣을지 결정
        # n=5이고 (0,0,0,0,4)이면, 0에 4개, 5개 1개
        cnt = Counter(comb)
        # cnt = K점수에 화살이 몇개 들어가는지
        ryan, apeach = 0, 0
        for i in range(1, 11):
            # info 배열 거꾸로, idx = 0 = 10점
            if info[10 - i] < cnt[i]:
                # cnt[i] = i번째가 key로 있음 value값 변환, 없으면 0
                ryan += i
            elif info[10 - i] > 0:
                apeach += i

        diff = ryan - apeach
        if diff > max_diff:
            max_comb_cnt = cnt
            max_diff = diff

    if max_diff > 0:
        answer = [0] * 11
        for n in max_comb_cnt:
            answer[10 - n] = max_comb_cnt[n]
        return answer
    else:
        return [-1]

solution(5,	[2,1,1,1,0,0,0,0,0,0,0])