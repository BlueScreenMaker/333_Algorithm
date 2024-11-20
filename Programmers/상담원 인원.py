import heapq
from collections import defaultdict
from itertools import combinations_with_replacement


def solution(k, n, reqs):
    answer = int(1e9)

    type_list = defaultdict(list)

    # k개 일단 n명 중에서 커버치고 남은 인원이 어떤 유형 커버칠지 정함
    combi = combinations_with_replacement([i for i in range(k)], r=n-k)

    arrange_people = []
    for check in combi:
        num_of_people = [1 for _ in range(k)]
        for idx in check:
            # 유형 중에 지원 오는 인원들
            num_of_people[idx] += 1
        arrange_people.append(num_of_people)

    for i in range(len(reqs)):
        start, during, consulting_type = reqs[i]
        type_list[consulting_type-1].append([start, during+start])

    for check in arrange_people:
        total = 0

        for i in range(k):
            mento_list = []
            for _ in range(check[i]):
                heapq.heappush(mento_list, 0)

            for start, end in type_list[i]:
                mento = heapq.heappop(mento_list)

                if mento < start:
                    heapq.heappush(mento_list, end)
                else:
                    wait = mento - start
                    total += wait
                    heapq.heappush(mento_list, end + wait)

        answer = min(answer, total)

    return answer

# https://minjiwoo.kr/565
print(solution(3, 5, [[10, 60, 1], [15, 100, 3], [20, 30, 1], [30, 50, 3], [50, 40, 1], [60, 30, 2], [65, 30, 1], [70, 100, 2]]))