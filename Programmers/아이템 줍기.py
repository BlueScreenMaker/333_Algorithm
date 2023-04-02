from collections import deque

max_value = 102  # 1칸 차이나는 경우, 붙는 것으로 판정되는 일이 생김
def solution(rectangle, characterX, characterY, itemX, itemY):
    board = [[0] * max_value for _ in range(max_value)]
    for x1, y1, x2, y2 in rectangle:
        dx1 = x1 * 2
        dy1 = y1 * 2
        dx2 = x2 * 2
        dy2 = y2 * 2
        for x in range(dx1, dx2+1):
            for y in range(dy1, dy2+1):
                # 테투리 채우기
                if dx1 < x < dx2 and dy1 < y <dy2:
                    board[x][y] = 0
                elif board[x][y] != 0:
                    board[x][y] = 1
    answer = bfs(characterX, characterY, itemX,itemY,board)
    return answer

dx = [-1,1,0,0]
dy = [0,0,-1,1]
visited = [[1] * max_value for _ in range(max_value)]
def bfs(start_x, start_y, end_x, end_y, board):
    que = deque()
    que.append([start_x * 2, start_y * 2])
    while que:
        px, py = que.popleft()
        if px == end_x * 2 and py == end_y * 2:
            return visited[px][py] // 2

        for i in range(4):
            nx = px + dx[i]
            ny = py + dy[i]
            if board[nx][ny] == 1 and visited[nx][ny] == 1:
                que.append([nx,ny])
                visited[nx][ny] = visited[px][py] + 1
    return

print(solution([[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]], 1, 3, 7, 8))