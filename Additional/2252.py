import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split(" "))

height = [[] for _ in range(N+1)]
deep = [0 for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, sys.stdin.readline().split(" "))
    height[A].append(B)
    deep[B] += 1

result = []
que = deque()
for i in range(1,N+1):
    if deep[i] == 0:
        que.append(i)
while que:
    now = que.popleft()
    result.append(now)
    for check in height[now]:
        deep[check] -= 1
        if deep[check] == 0:
            que.append(check)

print(' '.join(map(str, result)))