from collections import deque

def bfs(relation, gates, summits, value):
    que = deque(gates)
    while que:
        flag = que.popleft()
        if flag in summits:
            continue
        for node, cost in relation[flag]:
            temp = max(value[flag], cost)
            if value[node] > temp:
                que.append(node)
                value[node] = temp
    return value

def solution(n, paths, gates, summits):
    relation = [[] for _ in range(n+1)]
    for n1, n2, cost in paths:
        relation[n1].append([n2, cost])
        relation[n2].append([n1, cost])

    value = [ int(1e9) for _ in range(n+1) ]
    for i in gates:
        value[i] = 0

    # 리스트에 요소가 있는지 없는지 판단하는 시간 복잡도 O(N)
    # 딕셔너리에 키가 있는지 없는지 판단하는 시간 복잡조 O(1)
    sub_dic = {}
    for check in summits:
        sub_dic[check] = 1

    result = bfs(relation, gates, sub_dic, value)

    intensity = int(1e9)
    target = 0
    for goal in summits:
        if intensity > result[goal]:
            intensity = result[goal]
            target = goal
        elif intensity == result[goal] and target > goal:
            target = goal

    return [target, intensity]


print(solution(7,[[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]],[1],[2,3,4]))