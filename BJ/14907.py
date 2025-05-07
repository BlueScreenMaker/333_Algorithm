from collections import defaultdict, deque
import sys

taken_time = {}
indegree = defaultdict(int)
graph = defaultdict(list)
earliest = {}

# 입력 파싱
lines = sys.stdin.read().splitlines()

for line in lines:
    temp = list(line.split())
    
    job = temp[0]    
    taken_time[job] = int(temp[1])
    indegree[job] = 0
    earliest[job] = 0
    
    if len(temp) > 2:
        for condition in temp[-1]:
            graph[condition].append(job)
            indegree[job] += 1
            
que = deque()

# 진입 차수가 1인 것 부터 처리
for check_job in taken_time:
    if indegree[check_job] == 0:
        que.append(check_job)
        earliest[check_job] = taken_time[check_job]

while que:
    now = que.popleft()
    for next_node in graph[now]:
        earliest[next_node] = max(earliest[next_node], earliest[now] + taken_time[next_node])
        indegree[next_node] -= 1
        if indegree[next_node] == 0:
            que.append(next_node)

print(max(earliest.values()))