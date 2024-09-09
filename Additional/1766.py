import sys
import heapq

N, M = map(int,sys.stdin.readline().split(" "))

precede = [[] for _ in range(N+1)]
deep = [ 0 for _ in range(N+1)]

for _ in range(M):
    A, B = map(int,sys.stdin.readline().split(" "))
    precede[A].append(B)
    deep[B] += 1

que = []
for a in range(1,N+1):
    if deep[a] == 0:
        heapq.heappush(que, a)

result = []
while que:
    now = heapq.heappop(que)
    result.append(now)
    for check in precede[now]:
        deep[check] -= 1
        if deep[check] == 0:
            heapq.heappush(que, check)

print(' '.join(map(str,result)))