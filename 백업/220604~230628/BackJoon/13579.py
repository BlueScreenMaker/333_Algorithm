import sys
from collections import deque

N,K = map(int, sys.stdin.readline().split())

que=deque()
max_value=100001
que.append(N)
visited = [-1 for _ in range(max_value)]
visited[N] = 0

while que:
    pos = que.popleft()
    if pos == K:
        print(visited[K])
        break
    if 0 <= pos-1 < max_value and visited[pos-1] == -1:
        visited[pos-1] = visited[pos] + 1
        que.append(pos-1)
    if 0 < pos*2 < max_value and visited[pos*2] == -1:
        visited[pos*2] = visited[pos]
        que.appendleft(pos*2)
    if 0 <= pos+1 < max_value and visited[pos+1] == -1:
        visited[pos+1] = visited[pos] + 1
        que.append(pos+1)