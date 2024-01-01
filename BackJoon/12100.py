import sys
import copy

N = int(sys.stdin.readline())

# https://aia1235.tistory.com/44

board = []
for i in range(N):
    board.append(list(map(int, sys.stdin.readline().split(" "))))


def left(new_board):
    for i in range(N):
        point = 0
        for j in range(N):
            if new_board[i][j] != 0:
                tmp = new_board[i][j]
                new_board[i][j] = 0

                # 옆집이 비어있으면 복사해둔 값을 넣고
                if new_board[i][point] == 0:
                    new_board[i][point] = tmp

                # 옆집에 같은 값이 있으면 합쳐
                elif new_board[i][point] == tmp:
                    new_board[i][point] *= 2
                    point += 1

                # 옆집에 값도 있는데 같은 값 아니면
                # 옆집 바로 옆에 찰싹 붙여버림
                else:
                    point += 1 # pass
                    new_board[i][point] = tmp
    return new_board

def right(new_board):
    for i in range(N):
        point = N - 1
        for j in range(N - 1, -1, -1):

            if new_board[i][j] != 0:
                tmp = new_board[i][j]
                new_board[i][j] = 0

                if new_board[i][point] == 0:
                    new_board[i][point] = tmp

                elif new_board[i][point] == tmp:
                    new_board[i][point] *= 2
                    point -= 1
                else:
                    point -= 1
                    new_board[i][point] = tmp
    return new_board

def up(new_board):
    for j in range(N):
        point = 0
        for i in range(N):
            if new_board[i][j] != 0:
                tmp = new_board[i][j]
                new_board[i][j] = 0

                if new_board[point][j] == 0:
                    new_board[point][j] = tmp

                elif new_board[point][j] == tmp:
                    new_board[point][j] *= 2
                    point += 1

                else:
                    point += 1
                    new_board[point][j] = tmp
    return new_board

def down(new_board):
    for j in range(N):
        point = N - 1
        for i in range(N - 1, -1, -1):
            if new_board[i][j] != 0:
                tmp = new_board[i][j]
                new_board[i][j] = 0

                if new_board[point][j] == 0:
                    new_board[point][j] = tmp

                elif new_board[point][j] == tmp:
                    new_board[point][j] *= 2
                    point -= 1

                else:
                    point -= 1
                    new_board[point][j] = tmp
    return new_board

answer = 0
def dfs(n, temp_board):
    global answer
    if n == 5:
        max_value = max(map(max, temp_board))
        answer = max(answer, max_value)
        return answer

    for i in range(4):
        copy_board = copy.deepcopy(temp_board)
        if i == 0:
            dfs(n + 1, left(copy_board))
        elif i == 1:
            dfs(n + 1, right(copy_board))
        elif i == 2:
            dfs(n + 1, up(copy_board))
        else:
            dfs(n + 1, down(copy_board))

dfs(0, board)
print(answer)