import sys
sys.setrecursionlimit(10 ** 6)

N, K = map(int, sys.stdin.readline().split())

time = []
for _ in range(N):
    time.append(list(map(int, sys.stdin.readline().rstrip().split(" "))))

for i in range(N):
    for j in range(N):
        for k in range(N):
            time[i][j] = min(time[i][j], time[i][k]+time[k][j])

answer = N * 10000
visited = [False for _ in range(N)]
def find_path(plant, count, total):
    global answer
    # 왜 바로 return에다 total 넣으면 None로 반환되는지 모르겠다.
    if count==N:
        answer = min(answer, total)
        return
    else:
        for next in range(N):
            if not visited[next]:
                visited[next] = True
                find_path(next, count+1, total+time[plant][next])
                visited[next] = False

visited[K] = True
find_path(K,1,0)
print(answer)