from collections import deque
from math import inf
from copy import deepcopy
import sys
sys.setrecursionlimit(10**6)

def card_path(board, cx, cy, tx, ty):
    dy = [1, 0, 0, -1]
    dx = [0, 1, -1, 0]
    que = deque()
    que.append([cy, cx])
    visited = [[inf for _ in range(4)] for _ in range(4)]
    visited[cy][cx] = 0

    while que:
        py, px = que.popleft()
        if py == ty and px == tx:
            return visited[py][px]

        # 일반 이동
        for i in range(4):
            ny = py + dy[i]
            nx = px + dx[i]
            # 최소 거리를 구해야하니 이전것 보다 한 단계 전진해도 안커야함
            if 0 <= ny < 4 and 0 <= nx <4 and visited[ny][nx] > visited[py][px] + 1:
                visited[ny][nx] = visited[py][px] + 1
                que.append([ny, nx])

        # Ctrl 이동
        for i in range(4):
            ny = py + dy[i]
            nx = px + dx[i]
            while 0 <= ny + dy[i] < 4 and 0 <= nx + dx[i] < 4 and board[ny][nx] == 0:
                ny = dy[i] + ny
                nx = dx[i] + nx
            if 0 <= ny < 4 and 0 <= nx < 4 and visited[ny][nx] > visited[py][px] + 1:
                visited[ny][nx] = visited[py][px] + 1
                que.append([ny, nx])

def get_partner(board, target):
    for i in range(4):
        for j in range(4):
            if board[i][j] == target:
                return i, j

def empty_board(board):
    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                return False
    return True


answer = inf
def dfs(board, c, r, x, y, count):
    global answer
    copy_board = deepcopy(board)
    target = board[y][x]

    # 첫번째 카드
    count += card_path(copy_board, c, r, x, y)
    copy_board[y][x] = 0

    # 두번째 카드
    sy, sx = get_partner(copy_board, target)
    count += card_path(copy_board, x, y, sx, sy)
    copy_board[sy][sx] = 0

    count += 2

    if empty_board(copy_board):
        answer = min(answer, count)
    for i in range(4):
        for j in range(4):
            if copy_board[i][j] != 0:
                dfs(copy_board, sx, sy, j, i, count)

def solution(board, r, c):
    for i in range(4):
        for j in range(4):
            # 카드가 존재
            if board[i][j] != 0:
                dfs(board, c, r, j, i, 0)

    return answer


print(solution([[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]], 1, 0))
print(solution([[3,0,0,2],[0,0,1,0],[0,1,0,0],[2,0,0,3]], 0, 1))