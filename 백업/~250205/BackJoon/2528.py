import sys

N, L = map(int, sys.stdin.readline().split(" "))

info_bridge = []

for _ in range(N):
    info_bridge.append(list(map(int, sys.stdin.readline().split(" "))))

location_bridge = [[0,0,0]]
for i in range(N):
    len_bridge, start_point = info_bridge[i]
    # 1이면 > 오른쪽부터
    if start_point:
        location_bridge.append([L-len_bridge, L, start_point])
    else:
        location_bridge.append([0, len_bridge, start_point])

person = 1
flag = False
def up():
    global person
    global flag
    while True:
        if person == N:
            flag = True
            break

        c_start, c_end, c_direction = location_bridge[person]
        n_start, n_end, n_direction = location_bridge[person+1]

        if (c_end >= n_start and c_end <= n_end) or (c_start >= n_start and c_start <= n_end):
            person += 1
        elif c_start >= n_start and c_end <= n_end:
            person += 1
        elif c_start < n_start and c_end > n_end:
            person += 1
        else:
            break

def move():
    for i in range(1, N+1):
        start, end, direction = location_bridge[i]
        # 1 인 경우
        if direction:
            start -= 1
            end -= 1
            location_bridge[i] = [start, end, direction]
            if start == 0:
                location_bridge[i] = [start, end, 0]
        else:
            start += 1
            end += 1
            location_bridge[i] = [start, end, direction]
            if end == L:
                location_bridge[i] = [start, end, 1]

time_count = -1
while True:
    time_count += 1
    up()
    move()
    if flag:
        print(time_count)
        break
