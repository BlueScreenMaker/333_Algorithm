import sys

board = []
for i in range(5):
    board.append(list(map(int, sys.stdin.readline().split(" "))))

pos = list(map(int, sys.stdin.readline().split(" ")))
s1 = pos[:2]
s2 = pos[2:]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

count = [0,0]
flag = [True, True]
abs_count = 0
def dfs(x, y, ox, oy, pos):
    board[x][y] = -1
    temp = pos
    keeping = False
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 5 and 0 <= ny < 5:
            if board[nx][ny] == 0:
                keeping = True
                board[nx][ny] = -1
                temp = 0 if pos == 1 else 1
                dfs(ox,oy, nx, ny, temp)
                board[nx][ny] = 0
            elif board[nx][ny] == 1:
                keeping = True
                board[nx][ny] = -1
                count[pos] += 1
                temp = 0 if pos == 1 else 1
                dfs(ox, oy, nx, ny, temp)
                count[pos] -= 1
                board[nx][ny] = 1
    if not keeping:
        flag[pos] = False

    if not all(flag):
        abs_count = max(abs(count[0] - count[1]))
        return abs_count
    else:
        return True

mid_result = dfs(s1[0], s1[1], s2[0], s2[1], 0)
print(count)

if mid_result and (count[0] > count[1]):
    print(1)
else:
    print(0)
