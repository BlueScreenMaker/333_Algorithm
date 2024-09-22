from collections import deque

# 아래, 위, 왼쪽, 오른쪽
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def solution(board):
    length_row = len(board)
    length_col = len(board[0])
    start_x, start_y = 0, 0
    goal_x, goal_y = 0,0
    count = [[int(10e9) for _ in range(length_col)] for _ in range(length_row)]
    for i in range(length_row):
        for j in range(length_col):
            if board[i][j] == "R":
                start_x = i
                start_y = j
            elif board[i][j] == "G":
                goal_x = i
                goal_y = j

    que = deque()
    que.append((start_x, start_y, 0))
    count[start_x][start_y] = 0
    while que:
        cx, cy, cnt = que.popleft()
        if cx == goal_x and cy == goal_y:
            # print("\n".join(map(str, count)))
            return count[goal_x][goal_y]
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < length_row and 0 <= ny < length_col:
                # 위로 올라가기
                if i == 0:
                    if board[nx][ny] == ".":
                        for up in range(nx-1, -1, -1):
                            if board[up][ny] == "D":
                                temp = min(count[up+1][ny], cnt + 1)
                                count[up+1][ny] = temp
                                que.append((up+1, ny, temp))
                                break
                            elif up == 0 and board[0][ny] == ".":
                                temp = min(count[0][ny], cnt + 1)
                                count[0][ny] = temp
                                que.append((0, ny, temp))
                # 아래로 내려가기
                elif i == 1:
                    if board[nx][ny] == ".":
                        for down in range(nx+1, length_row):
                            if board[down][ny] == "D":
                                temp = min(count[down-1][ny], cnt + 1)
                                count[down-1][ny] = temp
                                que.append((down-1, ny, temp))
                                break
                            elif down == length_row-1 and board[0][length_row-1] == ".":
                                temp = min(count[down-1][ny], cnt + 1)
                                count[down-1][ny] = temp
                                que.append((length_row-1, ny, temp))
                # 왼쪽
                elif i == 2:
                    if board[nx][ny] == ".":
                        for left in range(ny-1, -1, -1):
                            if board[nx][left] == "D":
                                temp = min(count[nx][left+1], cnt + 1)
                                count[nx][left+1] = temp
                                que.append((nx, left+1, temp))
                                break
                            elif left == 0 and board[nx][0] == ".":
                                temp = min(count[nx][0], cnt+1)
                                count[nx][0] = temp
                                que.append((nx, 0, temp))
                #오른쪽
                else:
                    if board[nx][ny] == ".":
                        for right in range(ny+1, length_col):
                            if board[nx][right] == "D":
                                temp = min(count[nx][right-1], cnt+1)
                                count[nx][right-1] = temp
                                que.append((nx, right-1, cnt))
                                break
                            elif right == length_col - 1 and board[nx][length_col-1] == ".":
                                temp = min(count[nx][length_col-1], cnt+1)
                                count[nx][length_col-1] = temp
                                que.append((nx, length_col-1, cnt))

    return -1


print(solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]))
