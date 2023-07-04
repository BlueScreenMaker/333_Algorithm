def attach(x, y, M, key, board):
    for i in range(M):
        for j in range(M):
            board[x+i][y+j] += key[i][j]

def detach(x, y, M, key, board):
    for i in range(M):
        for j in range(M):
            board[x+i][y+j] -= key[i][j]

def check(board, M, N):
    for i in range(N):
        for j in range(N):
            if board[M+i][M+j] != 1:
                return False
    return True

def rotated(arr):
    n = len(arr)
    m = len(arr[0])
    result = [[0] * n for _ in range(m)]

    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = arr[i][j]
    return result


def solution(key, lock):
    N = len(lock)
    M = len(key)

    board = [[0] * (M*2 + N) for _ in range(M*2 + N)]

    for i in range(N):
        for j in range(N):
            board[M+i][M+j] = lock[i][j]

    key_rotated = key

    for a in range(4):
        key_rotated = rotated(key_rotated)
        for x in range(1, M+N):
            for y in range(1, M+N):
                attach(x, y, M, key_rotated, board)
                if (check(board, M, N)):
                    return True
                detach(x, y, M, key_rotated, board)
    return False