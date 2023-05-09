from collections import deque

def solution(n, roads, sources, destination):
    answer = []
    visit = [-1]*(n+1)
    relation = [[] for _ in range(n+1)]
    for s, e in roads:
        relation[s].append(e)
        relation[e].append(s)

    que = deque([destination])
    visit[destination] = 0
    while que:
        node = que.popleft()
        for check in relation[node]:
            if visit[check] == -1:
                visit[check] = visit[node]+1
                que.append(check)
    for i in sources:
        answer.append(visit[i])

    return answer

print(solution(3, [[1, 2], [2, 3]], [2,3], 1))
print(solution(5, [[1, 2], [1, 4], [2, 4], [2, 5], [4, 5]], [1, 3, 5], 5))

'''
from collections import deque


def solution(n, roads, sources, destination):
    answer = []
    relation = [[] for _ in range(n+1)]

    for s, e in  roads:
        relation[s].append(e)
        relation[e].append(s)
    # visited = [False for _ in range(n + 1)]
    # print(check_path(relation, 1, visited, destination))
    for i in sources:
        visited = [False for _ in range(n + 1)]
        if i == destination:
            answer.append(0)
        else:
            answer.append(check_path(relation, i, visited, destination))


    return answer

def check_path(node, start, visited, dest):
    que = deque()
    que.append(start)
    visited[start] = True
    count = 1
    while que:
        point = que.popleft()
        if dest in node[point]:
            return count
        else:
            for next in node[point]:
                if dest in node[next]:
                    return count + 1
                else:
                    que.append(next)
                    visited[next] = True
                    count += 1
    return -1
'''