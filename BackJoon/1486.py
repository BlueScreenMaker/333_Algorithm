import heapq
import sys

N, M, T, D = map(int, sys.stdin.readline().split())

mountain = []
for _ in range(N):
    mountain.append(list(sys.stdin.readline().rstrip()))

for a in range(N):
    for b in range(M):
        if mountain[a][b].isupper():
            mountain[a][b] = ord(mountain[a][b]) - ord("A")
        else:
            mountain[a][b] = (ord(mountain[a][b]) - ord("a")) + 26


dx = [-1,1,0,0]
dy = [0,0,-1,1]
def Dijkstra(sx, sy):
    time = [[int(1e9) for _ in range(M)] for _ in range(N)]
    time[sx][sy] = 0

    que = []
    heapq.heappush(que, [0, sx, sy])

    while que:
        c_time, cx, cy = heapq.heappop(que)
        # 현재 시간보다 더 최소의 값으로 배열이 갱신되어있기 때문에 굳이 계산을 할 필요 없음
        # 일종의 visitied 조건
        if time[cx][cy] >= c_time:
            c_height = mountain[cx][cy]
            for i in range(4):
                nx = cx + dx[i]
                ny = cy + dy[i]
                if 0 <= nx < N and 0 <= ny < M:
                    n_height = mountain[nx][ny]
                    if abs(c_height - n_height) <= T:
                        if c_height >= n_height:
                            n_time = c_time + 1
                        else:
                            n_time = c_time + (c_height - n_height) ** 2

                        if time[nx][ny] > n_time:
                            time[nx][ny] = n_time
                            heapq.heappush(que, [n_time, nx, ny])
    return time

check_time = Dijkstra(0, 0)

candi = []
for i in range(N):
    for j in range(M):
        if check_time[i][j] < D:
            # 파이썬은 최소 heap만 제공해서 -1을 곱해야 최대 힙을 만들 수 있음
            m_height = -1 * mountain[i][j]
            heapq.heappush(candi, [m_height, i, j])

# 후보지들을 기준으로 시간 내에 돌아올 수 있는지 파악
while candi:
    pt, px, py = heapq.heappop(candi)
    possible_time = Dijkstra(px, py)
    # check_time: 0,0 > px,py
    # possible_time: px,py > 0,0
    if check_time[px][py] + possible_time[0][0] <= D:
        print(mountain[px][py])
        break
