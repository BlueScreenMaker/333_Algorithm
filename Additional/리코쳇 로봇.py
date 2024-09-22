from collections import deque

# 아래, 위, 왼쪽, 오른쪽
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def solution(board):
    length_row = len(board)
    length_col = len(board[0])
    start_x, start_y = 0, 0
    goal_x, goal_y = 0,0
    visited = [[ False for _ in range(length_col)] for _ in range(length_row)]
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
    visited[start_x][start_y] = True
    while que:
        cx, cy, cnt = que.popleft()
        if cx == goal_x and cy == goal_y:
            return cnt
        for i in range(4):
            # cx, cy 기준으로 갈 수 있는 방향을 다 구해야함
            nx = cx
            ny = cy
            # 한 방향으로 최대한 갈 수 있는 곳 까지 감
            # 이 때, 그 방향의 값이 'D'가 아니여야함
            while 0 <= nx+dx[i] < length_row and 0 <= ny+dy[i] < length_col and board[nx+dx[i]][ny+dy[i]] != "D":
                # 최대한 갈 수 있을 때 까지 nx와 ny값 증가.
                nx += dx[i]
                ny += dy[i]
            # 최종 도착 지점이 방문한 지점인가요?
            if not visited[nx][ny]:
                # 아니면 방문한 지점으로 체크해주고 넣어줌.
                visited[nx][ny] = True
                que.append((nx,ny,cnt+1))
            # 방문한 지점이면 추가 하지 않음

    return -1


print(solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]))
