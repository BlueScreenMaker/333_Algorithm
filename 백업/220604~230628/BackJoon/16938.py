import sys
import itertools

N,L,R,X = map(int, sys.stdin.readline().split())

level = list(map(str, sys.stdin.readline().split()))

combi = []
for i in range(2, len(level)+1):
    temp = itertools.combinations(level,i)
    combi.extend(temp)

count = 0

for check in combi:
    values = list(map(int, check))
    total = sum(values)
    diff = max(values)-min(values)
    if L <= total <= R and diff >= X:
        count += 1

print(count)