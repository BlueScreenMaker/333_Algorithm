import sys
sys.setrecursionlimit(10 ** 6)

def dfs(node, result):
    visited[node] = True
    cycle.append(node)
    check = about[node]
    if visited[check]:
        if check in cycle:
            result += cycle[cycle.index(check):]
        return
    else:
        dfs(check, result)

T = int(sys.stdin.readline())

for i in range(T):
    N = int(sys.stdin.readline())
    about = [0]
    about.extend(map(int, sys.stdin.readline().split(" ")))

    visited = [ False for _ in range(N+1)]

    result = []

    for j in range(1, N+1):
        if not visited[j]:
            cycle = []
            dfs(j, result)
    print(N-len(result))

'''
import sys
from collections import deque

T = int(sys.stdin.readline())

def bfs(start, cycle):
    que = deque()
    que.append(start)
    visited[start] = True
    cycle.append(start)
    count = 1
    while que:
        node = que.popleft()
        for check in relationship[node]:
            if check in cycle:
                if check == start:
                    return [True, cycle]
            elif not visited[check]:
                cycle.append(check)
                que.append(check)
                visited[check] = True
                count += 1
    return [False, cycle]

for i in range(T):
    N = int(sys.stdin.readline())
    about = list(map(int, sys.stdin.readline().split(" ")))

    relationship = [ [] for _ in range(N+1)]

    for j in range(N):
        relationship[j+1].append(about[j])

    visited = [ False for _ in range(N+1)]

    total = N
    result = []
    for h in range(1, N+1):
        if not visited[h]:
            cycle = []
            flag, temp = bfs(h, cycle)
            if not flag:
                for p in temp:
                    visited[p] = False
            else:
                total -= len(temp)

    print(total)
'''


