import sys

N, M = map(int, sys.stdin.readline().split())

num_list = []
for _ in range(N):
    num_list.append(int(sys.stdin.readline()))
num_list.sort()

start = 0
end = 0
result = int(1e9)

while start < N and end < N:
    diff = num_list[end] - num_list[start]
    if diff < M:
        end += 1
    else:
        result = min(result, diff)
        start += 1

print(result)