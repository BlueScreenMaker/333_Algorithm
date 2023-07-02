from collections import deque

def bfs(check,x,y):
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    que=deque()
    que.append([x,y])
    while que:
        px,py=que.popleft()
        for i in range(4):
            nx=dx[i]+px
            ny=dy[i]+py
            if nx<0 or ny<0 or nx>=5 or ny>=5 or (nx==x and ny==y):
                continue

            # x와 y 기준으로 상하좌우를 살피는 중
            manhattan=abs(x-nx)+abs(y-ny)
            if check[nx][ny]=="P" and manhattan<=2:
                return False
            elif check[nx][ny]=="O" and manhattan<2:
                que.append([nx,ny])

    return True


def solution(places):
    answer = []

    for check in places:
        flag=True
        for x in range(5):
            if flag:
                for y in range(5):
                    if flag:
                        if check[x][y]=="P":
                            flag=bfs(check,x,y)
        if flag:
            answer.append(1)
        else:
            answer.append(0)

    return answer

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
               ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
               ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"]]))
