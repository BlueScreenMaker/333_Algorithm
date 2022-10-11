from collections import deque

def next_load(pos, board):
    next = []
    position = list(pos)
    pos1_x, pos1_y, pos2_x, pos2_y = position[0][0], position[0][1], position[1][0], position[1][1]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        pos1_next_x, pos1_next_y, pos2_next_x, pos2_next_y = pos1_x + dx[i], pos1_y + dy[i], pos2_x + dx[i], pos2_y + dy[i]
        # 이동하고자 하는 두 칸이 모두 비어 있다면
        if board[pos1_next_x][pos1_next_y] == 0 and board[pos2_next_x][pos2_next_y] == 0:
            next.append({(pos1_next_x, pos1_next_y), (pos2_next_x, pos2_next_y)})

    # 현재 로봇이 가로로 놓여 있는 경우
    if pos1_x == pos2_x:
        for i in [-1, 1]:  # 위쪽으로 회전하거나, 아래쪽으로 회전
            # 위쪽 혹은 아래쪽 두 칸이 모두 비어 있다면
            if board[pos1_x + i][pos1_y] == 0 and board[pos2_x + i][pos2_y] == 0:
                next.append({(pos1_x, pos1_y), (pos1_x + i, pos1_y)})
                next.append({(pos2_x, pos2_y), (pos2_x + i, pos2_y)})
    # 현재 로봇이 세로로 놓여 있는 경우
    elif pos1_y == pos2_y:
        for i in [-1, 1]:  # 왼쪽으로 회전하거나, 오른쪽으로 회전
            # 왼쪽 혹은 오른쪽 두 칸이 모두 비어 있다면
            if board[pos1_x][pos1_y + i] == 0 and board[pos2_x][pos2_y + i] == 0:
                next.append({(pos1_x, pos1_y), (pos1_x, pos1_y + i)})
                next.append({(pos2_x, pos2_y), (pos2_x, pos2_y + i)})
    # 현재 위치에서 이동할 수 있는 위치를 반환
    return next


def solution(board):
    answer = 0
    N = len(board)
    new_board = [ [1 for _ in range(N+2)] for _ in range(N+2) ]
    for x in range(N):
        for y in range(N):
            new_board[x+1][y+1]=board[x][y]

    que = deque()
    visited = []

    # I don't know dict
    pos = {(1,1),(1,2)}

    que.append((pos, 0))

    visited.append(pos)

    while que:
        pos, count = que.popleft()
        if (N, N) in pos:
            return count
        for next_pos in next_load(pos, new_board):
            if next_pos not in visited:
                que.append((next_pos, count+1))
                visited.append(next_pos)

    return 0

print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))