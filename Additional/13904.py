import heapq
import sys

N = int(sys.stdin.readline())

task = []
total_day = 0
for _ in range(N):
    d, w = map(int, sys.stdin.readline().split())
    heapq.heappush(task, (-w, d))
    if total_day < d:
        total_day = d

result = [0 for _ in range(total_day+1)]
while task:
    w, d = heapq.heappop(task)
    for day in range(d, 0, -1):
        if not result[day]:
            result[day] = -w
            break
        else:
            if result[day] < -w:
                result[day] = -w

print(sum(result))