import sys
from itertools import combinations

N, C = map(int, sys.stdin.readline().split(" "))
# N: 물건 수
# C: 최대 무게

stuff = list(map(int, sys.stdin.readline().split(" ")))

# 시초 이슈로 반으로 쪼개기
half_1 = stuff[:N//2]
half_2 = stuff[N//2:]

sub_sum_1 = []
sub_sum_2 = []

for a in range(len(half_1) + 1):
    comb_a = combinations(half_1, a)
    for comb in comb_a:
        sub_sum_1.append(sum(comb))

for b in range(len(half_2) + 1):
    comb_b = combinations(half_2, b)
    for comb in comb_b:
        sub_sum_2.append(sum(comb))

sub_sum_1.sort()
sub_sum_2.sort()
answer = 0

for check in sub_sum_2:
    if check > C:
        continue

    start = 0
    end = len(sub_sum_1) - 1

    while start <= end:
        mid = (start + end) // 2
        if sub_sum_1[mid] + check > C:
            end = mid - 1
        else:
            start = mid + 1
    answer += end + 1

print(answer)
