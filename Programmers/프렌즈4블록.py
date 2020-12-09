from collections import deque

way=[[0,-1],[+1,-1],[+2,0],[+2,+1],[0,+2],[+1,+2],[-1,0],[-1,+1]]

def check(m,n,block):
    queue=deque()

    return

def solution(m, n, board):
    block=[]
    for a in range(0,m):
        s=board[a]
        block.append(list(s))

    for i in range(0,m-1):
        for j in range(0,n-1):
            if block[i][j]==block[i][j+1]==block[i+1][j]==block[i+1][j+1]:
                check(i,j,block)
                print("4블록")
    answer = 0
    return answer


print(solution(6,6,["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))