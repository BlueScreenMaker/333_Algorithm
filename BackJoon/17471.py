import sys
import itertools
from collections import deque


def bfs(combi):
    start = combi[0]
    visited = set([start])
    que = deque([start])
    total = 0
    while que:
        node = que.popleft()
        total += people[node]
        for check in relation[node]:
            if check not in visited and check in combi:
                que.append(check)
                visited.add(check)

    return total, len(visited)


N = int(sys.stdin.readline())

people = list(map(int, sys.stdin.readline().split()))
people.insert(0,0)


relation = [ [0] ]
for i in range(N):
    tmp = [int(x) for x in sys.stdin.readline().split()]
    setting = []
    for j in range(1,len(tmp)):
        setting.append(tmp[j])
    relation.append(setting)

answer = int(1e9)
for i in range(1, N//2+1):
    combi_list = list(itertools.combinations(range(1,N+1), i))
    for combi in combi_list:
        population1, visit1 = bfs(combi)
        other = []
        for j in range(1,N+1):
            if j not in combi:
                other.append(j)
        population2, visit2 = bfs(other)

        if visit1 + visit2 == N:
            answer = min(answer, abs(population1-population2))

if answer == int(1e9):
    print(-1)
else:
    print(answer)
