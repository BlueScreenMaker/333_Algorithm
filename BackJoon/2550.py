import sys

# 0 0 4
def Track(start, end, point):
    global lower
    if start > end:
        return
    m = (start + end) // 2

    if LIS[m] > point:
        lower = m
        Track(start, m - 1, point)
    else:
        Track(m + 1, end, point)


N=int(sys.stdin.readline())

switch=list(map(int, sys.stdin.readline().split(" ")))
light=list(map(int, sys.stdin.readline().split(" ")))

relationship=[0 for _ in range(N+1)]

for i, j in enumerate(light):
    # i = index // v = light[i]
    relationship[j] = i + 1

print(relationship)

LIS = []
track = []
lower = 0

for i in switch:
    temp = relationship[i]
    if len(LIS) == 0 or LIS[-1] < temp:
        track.append(len(LIS))
        LIS.append(temp)
    else:
        Track(0, len(LIS) - 1, temp)
        LIS[lower] = temp
        track.append(lower)

result = []
check = max(track)
for j in track[::-1]:
    N -= 1
    if check == j:
        result.append(switch[N])
        check -= 1

print(len(result))
print(' '.join(map(str, sorted(result))))

