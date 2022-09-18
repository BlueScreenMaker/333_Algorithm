import sys

N, M = map(int, sys.stdin.readline().split())

lamp = []
for i in range(N):
    lamp.append(list(sys.stdin.readline().rstrip()))

K = int(sys.stdin.readline())

answer = 0
for check in lamp:
    zero_count = check.count('0')
    if zero_count <= K and zero_count%2 == K%2:
        same = 0
        for s in lamp:
            if check == s:
                same += 1
        if same > answer:
            answer = same

print(answer)