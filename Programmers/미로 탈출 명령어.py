import sys
sys.setrecursionlimit(10**5)

command = ["d","l","r","u"]
dx = [1, 0, 0, -1]
dy = [0, -1, 1, 0]

answer = []

def checking(n,m,cx,cy,r,c,k,dist,path):
    global flag
    if flag or abs(cx-r) + abs(cy-c) + dist > k:
        return
    if dist == k:
        if (cx, cy) == (r, c):
            flag = True
            answer.append(path)
        return

    for i in range(4):
        nx = cx + dx[i]
        ny = cy + dy[i]
        if 0 < nx <= n and 0 < ny <= m:
            checking(n,m,nx,ny,r,c,k,dist+1,path+command[i])

def solution(n, m, x, y, r, c, k):
    remain = k - abs(x-r) + abs(y-c)
    if remain < 0 or remain % 2 != 0:
        return "impossible"

    global flag
    flag = False
    checking(n,m,x,y,r,c,k,0,"")

    if not answer:
        return "impossible"

    else:
        return answer[0]


print(solution(3,4,2,3,3,1,5))