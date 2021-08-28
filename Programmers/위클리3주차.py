from collections import deque

global answer
answer=[]


dx=[-1,+1,0,0]
dy=[0,0,-1,+1]
def bfs(x,y,board,visited,empty, check,N):
    result=[]
    que=deque()
    que.append([x,y])
    while que:
        nx,ny=que.popleft()
        for i in range(4):
            px=nx+dx[i]
            py=ny+dy[i]
            if px<0 or py<0 or px>=N or py>=N:
                continue
            else:
                if visited[px][py]==False and board[px][py]==check:
                    result.append([nx,ny])
                    visited[px][py]=True
                    que.append([px,py])
    empty.append(sorted(result))

def change(b):
    temp=[]
    if b:
        cx=b[0][0]
        cy=b[0][1]
        for ax, ay in b:
            temp.append([ax-cx,ay-cy])
    return sorted(temp)

def rotate(b,N):
    new_b=[]
    for x,y in b:
        new_b.append([y,N-1-x])
    return change(new_b)

def matching(b,N,empty_b):
    for t in range(N):
        for h in range(N):
            match=[]
            for x,y in b:
                check_x=t+x
                check_y=h+y
                if check_x<0 or check_y<0 or check_y>=N or check_x>=N:
                    break
                else:
                    match.append([check_x,check_y])
            if len(b)==len(match) and match in empty_b:
                empty_b.remove(match)
                answer.extend(match)
                return True
    return False


def solution(game_board, table):

    N=len(game_board)

    visited_b=[[False for _ in range(N)] for _ in  range(N)]
    visited_t=[[False for _ in range(N)] for _ in  range(N)]

    empty_b=[]
    empty_t=[]

    for i in range(N):
        for j in range(N):
            if visited_b[i][j]==False and game_board[i][j]==0:
                bfs(i,j,game_board,visited_b,empty_b,0,N)
            if visited_t[i][j]==False and table[i][j]==1:
                bfs(i,j,table,visited_t,empty_t,1,N)


    block=[]

    for a in empty_t:
        block.append(change(a))


    for z in block:
        for w in range(4):
            if matching(z,N,empty_b)==False:
                z=rotate(z,N)

            else:
                break


    print(len(answer))
    return len(answer)

solution([[0,0,1,0,1,0,1,0,1,0,1,0,0,1,0,0,0,0], [1,0,0,0,1,0,1,0,1,0,1,0,0,1,0,1,1,1], [0,1,1,1,0,0,1,0,1,0,0,1,1,0,1,0,0,0], [0,0,0,0,1,1,0,0,1,1,0,1,0,0,1,0,0,0], [0,1,1,1,0,0,1,1,1,1,0,1,1,1,0,1,1,1], [1,0,1,0,0,0,1,0,0,0,1,0,0,0,0,1,0,0], [0,0,0,1,1,1,0,0,1,1,0,1,1,1,1,0,0,1], [1,1,1,0,0,0,1,1,0,0,1,0,0,0,0,1,1,0], [0,0,1,0,1,1,1,0,0,1,0,1,1,1,1,0,0,0], [1,1,0,1,1,0,1,1,1,1,0,1,0,0,0,1,1,1], [0,0,0,0,1,0,0,0,0,1,0,1,0,0,1,0,1,0], [1,1,1,1,0,1,1,1,1,1,0,1,0,1,0,0,1,0], [0,0,1,0,0,0,1,0,0,0,1,0,1,0,1,1,0,0], [1,0,1,1,0,1,1,0,0,0,1,0,0,0,1,0,0,1], [1,0,0,1,1,0,0,1,1,1,0,1,1,1,0,1,1,0], [0,1,1,0,0,1,0,1,0,0,1,0,0,0,0,0,1,0], [0,0,0,1,0,1,0,1,0,0,1,1,1,1,1,1,1,0], [0,1,0,1,1,0,0,1,0,1,0,0,0,0,0,0,1,0]]
         ,
         [[1,1,1,1,1,1,0,1,0,1,1,0,0,1,0,0,1,0], [0,0,0,0,0,0,1,1,1,0,1,0,1,1,0,1,1,0], [1,0,1,1,0,1,0,1,0,1,1,0,1,0,1,1,0,1], [1,1,0,1,1,1,0,1,0,1,0,1,1,0,1,0,0,1], [1,1,1,0,0,0,1,0,1,0,1,0,0,1,0,0,1,1], [0,0,0,1,1,1,0,1,1,1,0,1,1,0,1,0,0,0], [1,1,1,0,0,0,0,0,1,1,0,1,1,0,1,1,1,1], [0,0,1,0,1,1,0,1,0,0,1,0,0,1,0,0,0,0], [1,0,1,0,0,0,0,1,0,1,1,0,1,1,0,1,1,1], [1,0,1,0,1,1,1,1,0,1,1,0,0,0,1,1,1,0], [1,1,0,1,0,0,0,0,1,0,0,1,1,1,0,0,0,0], [0,0,1,1,1,1,0,1,1,0,1,0,0,0,1,1,0,1], [1,1,0,1,0,0,1,0,0,1,0,1,0,1,0,1,0,1], [1,1,0,0,1,1,1,0,1,1,0,1,0,1,0,1,0,1], [0,0,1,1,0,1,1,0,1,0,1,1,0,0,0,1,0,0], [1,1,1,0,1,0,0,1,0,1,1,0,0,1,0,1,0,1], [0,0,0,0,1,0,1,1,1,0,0,1,0,1,1,0,1,1], [0,1,1,1,1,0,0,1,0,0,1,1,0,1,0,0,1,1]])