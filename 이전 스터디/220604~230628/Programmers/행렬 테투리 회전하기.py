def solution(rows, columns, queries):
    answer = []
    board=[[0 for _ in range(columns+1)] for _ in range(rows+1)]
    count=1
    for i in range(1,rows+1):
        for j in range(1,columns+1):
            board[i][j]=count
            count+=1

    for sx,sy,ex,ey in queries:
        standard=board[sx][sy]
        min_value=standard

        # 왼쪽 : 아래 → 위
        for i in range(sx,ex):
            temp=board[i+1][sy]
            board[i][sy]=temp
            min_value=min(min_value,temp)

        # 아래 : 오른쪽 → 왼쪽
        for j in range(sy,ey):
            temp=board[ex][j+1]
            board[ex][j]=temp
            min_value=min(min_value,temp)
            
        # 왼쪽 : 위 → 아래
        for w in range(ex,sx,-1):
            temp=board[w-1][ey]
            board[w][ey]=temp
            min_value=min(min_value,temp)
        
        #위 : 왼 → 오
        for z in range(ey,sy,-1):
            temp=board[sx][z-1]
            board[sx][z]=temp
            min_value=min(min_value,temp)
            
        board[sx][sy+1]=standard
        answer.append(min_value)

    return answer

print(solution(100,97,[[1,1,100,97]]	))