def check(m,n,block):
    if block[m][n]==block[m][n+1]==block[m+1][n+1]:
        print("옆과 아래에 같은 블록 있음")
    elif block[m+1][n]==block[m+1][n+1]:
        print("블록 확인")

    return

def solution(m, n, board):
    block=[]
    for a in range(0,m):
        s=board[a]
        block.append(list(s))

    for i in range(0,m-1):
        for j in range(0,n-1):
            if block[i][j]==block[i][j+1]==block[i+1][j]==block[i+1][j+1]:
                check(i,j+1,block)
                print("4블록")
    answer = 0
    return answer


print(solution(6,6,["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))