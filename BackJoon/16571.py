import sys

def game(player, board):
    enemy_result = 2
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                board[i][j] = player
                if (checkmate(player, board)):
                    enemy_result = min(enemy_result, -1)
                next = 1 if player == 2 else 2
                enemy_result = min(enemy_result, game(next, board))
                board[i][j] = 0
    # 지는건 -1 /  0은 비기는거 /  1은 이기는거
    # 만약 board 다 차있어서 순환이 안된다면... 갱신이 안되어서 2가 되겠지.
    if enemy_result == 1:
        return -1
    elif enemy_result == 0 or enemy_result == 2:
        return 0
    else:
        return 1


def checkmate(player, board):
    # 가로
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True

    # 세로
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True

    # 대각선
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False

board = []
for i in range(3):
    board.append(list(map(int, sys.stdin.readline().split(" "))))

turn = 0
for i in range(3):
    for j in range(3):
        if board[i][j] == 1 or board[i][j] == 2:
            turn += 1
# 전체 턴 수가
# 짝수 이면, X가 다음 턴이기 때문에 1
# 홀수 이면 O가 다음 턴이기 때문에 2
start = 1 if turn % 2 ==0 else 2

play_result = game(start, board)
if play_result== 1:
    print("W")
elif play_result == 0:
    print("D")
else:
    print("L")