from collections import deque
import copy

global answer
answer = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
empty_g = []
block_t = []


def bfs(x, y, N, visited, array, check):
    space = []
    que = deque()
    que.append([x, y])
    space.append([x, y])
    visited[x][y] = True
    while que:
        px, py = que.popleft()
        for i in range(4):
            nx = px + dx[i]
            ny = py + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if visited[nx][ny] == False and array[nx][ny] == check:
                visited[nx][ny] = True
                que.append([nx, ny])
                space.append([nx, ny])

    return sorted(space)


def rotate(b, N):
    new_board = []

    for block in b:
        new_board.append([block[1], -block[0]])

    return sorted(standard(new_board, N))


def standard(b, N):
    change = []
    minx = N
    miny = N
    for i in b:
        minx = min(minx, i[0])
        miny = min(miny, i[1])
    for x, y in b:
        change.append([x - minx, y - miny])
    return sorted(change)


def solution(game_board, table):
    global answer
    N = len(game_board)

    visited_g = [[False for _ in range(N)] for _ in range(N)]
    visited_t = [[False for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if game_board[i][j] == 0 and visited_g[i][j] == False:
                empty_g.append(bfs(i, j, N, visited_g, game_board, 0))
            if table[i][j] == 1 and visited_t[i][j] == False:
                block_t.append(bfs(i, j, N, visited_t, table, 1))
            else:
                continue

    table_block = []
    for a in block_t:
        table_block.append(standard(a, N))
    # table의 빈 블록을 가장 앞 좌표를 0,0 기준으로 전환

    game_block = []
    for b in empty_g:
        game_block.append(standard(b, N))

    for g_block in game_block:
        if g_block in table_block:
            answer += len(g_block)
            table_block.remove(g_block)
        else:
            flag = False
            for t_block in table_block:
                temp = copy.copy(t_block)
                for z in range(4):

                    if g_block == temp:
                        answer += len(g_block)
                        table_block.remove(t_block)
                        flag = True
                        break
                    temp = rotate(temp, N)
                if flag:
                    break

    return answer