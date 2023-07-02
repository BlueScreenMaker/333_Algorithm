import sys
sys.setrecursionlimit(10**5)

directions = ['d', 'l', 'r', 'u']
dx = [1, 0, 0, -1]
dy = [0, -1, 1, 0]

answer = []

def dfs(px, py, dist, path, flag, r, c, k, n, m):
    if flag[0] or abs(px - r) + abs(py - c) + dist > k:
        return

    if dist == k:
        if (px, py) == (r, c):
            flag[0] = True
            answer.append(path)
        return

    for i in range(4):
        nx = px + dx[i]
        ny = py + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            dfs(nx, ny, dist + 1, path + directions[i], flag, r, c, k, n, m)

def solution(n, m, x, y, r, c, k):
    remain = k - abs(x-r) + abs(y-c)
    if remain < 0 or remain % 2 != 0:
        return 'impossible'

    flag = [False]

    dfs(x - 1, y - 1, 0, '', flag, r-1, c-1, k, n, m)
    if not answer:
        return 'impossible'
    else:
        return answer[0]


print(solution(3,4,2,3,3,1,5))
# print(solution(2,2,1,1,2,2,2))
# print(solution(3,3,1,2,3,3,4))