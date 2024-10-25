import sys
from collections import deque

N = int(sys.stdin.readline())

precondition = [[] for _ in range(N+1)]
dp = [0 for _ in range(N+1)]
deep = [0 for _ in range(N+1)]
time = [0 for _ in range(N+1)]

for a in range(1, N+1):
    temp = list(map(int, sys.stdin.readline().split()))
    time[a] = temp[0]
    for b in temp[1:len(temp)-1]:
        precondition[b].append(a)
        deep[a] += 1

print(precondition)

que = deque()

for i in range(1, N+1):
    if not deep[i]:
        dp[i] = time[i]
        que.append(i)

while que:
    node = que.popleft()
    for j in precondition[node]:
        deep[j] -= 1
        dp[j] = max(dp[j], dp[node] + time[j])
        if not deep[j]:
            que.append(j)

print('\n'.join(map(str, dp[1:])))