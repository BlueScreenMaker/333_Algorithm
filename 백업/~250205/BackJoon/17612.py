import heapq
import sys

N, K = map(int, sys.stdin.readline().split(" "))
# 사람 수 N / 계산대 수 K

counter = []
finish = []

for i in range(N):
    id, stuff = map(int, sys.stdin.readline().split(" "))
    if len(counter) < K: # 계산대 비어있음
        # 물건 수, 계산대, 고객 아이디
        heapq.heappush(counter, [stuff, i+1, id])
    else:
        time, check_out, c_id = heapq.heappop(counter)
        # 대기 중인 고객 넣기
        heapq.heappush(counter, [stuff + time, check_out, id])
        # 빈 계산대 중 번호 큰것부터 앞으로 쭉쭉
        heapq.heappush(finish, [time, -check_out, c_id])

while counter:
    time, check_out, c_id = heapq.heappop(counter)
    heapq.heappush(finish, [time, -check_out, c_id])

answer = 0
for j in range(N):
    temp = heapq.heappop(finish)
    answer += temp[2] * (j+1)

print(answer)