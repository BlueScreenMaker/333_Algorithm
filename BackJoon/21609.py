import copy
import sqlite3
import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split(" "))

game_board = []
for i in range(N):
    game_board.append(list(map(int, sys.stdin.readline().split(" "))))

def bfs(start_x, start_y, color):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    que = deque()
    que.append([start_x, start_y])

    b_count, r_count =  1,0
    block, rainbow =  [[start_x,start_y]], []


    while que:
        px, py = que.popleft()
        for i in range(4):
            nx = px + dx[i]
            ny = py + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if not visited[nx][ny]:
                # 일반 블록인 경우
                if game_board[nx][ny] == color:
                    visited[nx][ny] = True
                    que.append([nx, ny])
                    b_count += 1
                    block.append([nx, ny])
                # 무지개 블록인 경우
                elif game_board[nx][ny] == 0:
                    visited[nx][ny] = True
                    que.append([nx, ny])
                    b_count += 1
                    r_count += 1
                    rainbow.append([nx,ny])

    for x, y in rainbow:
        visited[x][y] = False

    return [b_count, r_count, block + rainbow]

def remove_block(blocks):
    # 2. 블록 제거
    for bx, by in blocks:
        game_board[bx][by] = -2


# 3. 블록 내리기
def down_block(blocks):
    for i  in range(N-2, -1, -1):
        for j in range(N):
            if blocks[i][j] > -1:
                point = i
                while True:
                    if 0 <= point+1 < N and blocks[point+1][j] == -2:
                        blocks[point+1][j] = blocks[point][j]
                        blocks[point][j] = -2
                        point += 1
                    else:
                        break


def rotate_block(blocks):
    # 4. 90도 반시계 방향 회전
    # X,Y > N-Y-1, X
    new_board = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_board[N - j - 1][i] = blocks[i][j]
    return new_board


score = 0
while True:
    visited = [[False for _ in range(N)] for _ in range(N)]
    blocks = []
    for i in range(N):
        for j in range(N):
            if game_board[i][j] > 0 and not visited[i][j]:
                visited[i][j] = True
                block_info = bfs(i,j, game_board[i][j])
                #  [블록 크기, 무지개블록 개수, 블록좌표]
                if block_info[0] >= 2:
                    blocks.append(block_info)
    blocks.sort(reverse=True)

    if not blocks:
        break
    remove_block(blocks[0][2])
    score += blocks[0][0] ** 2

    down_block(game_board)
    game_board = rotate_block(game_board)
    down_block(game_board)

print(score)
