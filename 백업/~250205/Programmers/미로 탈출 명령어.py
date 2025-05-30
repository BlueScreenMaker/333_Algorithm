import sys
sys.setrecursionlimit(10**6)

command = ["d","l","r","u"]
dx = [1, 0, 0, -1]
dy = [0, -1, 1, 0]

def checking(n,m, cx, cy, r, c, k, dist, path):
    global flag
    if flag or abs(cx-r) + abs(cy-c) + dist > k:
        return

    if dist == k and cx == r and cy == c:
        flag = True
        answer.append(path)
        return

    for i in range(4):
        nx = cx + dx[i]
        ny = cy + dy[i]
        # idx가 1부터 시작
        if 0 < nx <= n and 0 < ny <= m:
            checking(n,m, nx, ny, r, c, k, dist+1, path+command[i])

answer = []
flag = False

def solution(n, m, x, y, r, c, k):
    global answer

    remain = k - abs(x-r) + abs(y-c)

    if remain < 0 or remain % 2 != 0:
        return "impossible"

    checking(n, m, x, y, r, c, k, 0, "")

    if answer:
        return answer[0]
    else:
        return "impossible"


print(solution(3,4,2,3,3,1,5))