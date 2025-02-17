import sys

N = int(sys.stdin.readline())
INF = 200_001

balls = []

for a in range(N):
    color, size = map(int, sys.stdin.readline().split())
    balls.append([a+1, color, size])

balls.sort(key=lambda x:x[2])
print(balls)

count = [0 for _ in range(INF)]
step = 0
total = 0
answer = [0 for _ in range(N+1)]
for i in range(N):
    while balls[step][2] < balls[i][2]:
        count[balls[step][1]] += balls[step][2]
        total += balls[step][2]
        step += 1
    answer[balls[i][0]] = total - count[balls[i][1]]

for b in range(1, N+1):
    print(answer[b])
