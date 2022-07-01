def solution(board, skill):
    answer = 0
    x=len(board)
    y=len(board[0])
    accum_sum=[ [ 0 for _ in range(y+1)] for _ in range(x+1)]

    for type_skill, r1,r2, c1,c2, degree in skill:
        c1+=1
        c2+=1
        if type_skill==1:
            accum_sum[r1][r2]-=degree
            accum_sum[c1][c2]-=degree
            accum_sum[r1][c2]+=degree
            accum_sum[c1][r2]+=degree
        else:
            accum_sum[r1][r2]+=degree
            accum_sum[c1][c2]+=degree
            accum_sum[r1][c2]-=degree
            accum_sum[c1][r2]-=degree

    # 위 → 아래
    for w in range(x):
        for h in range(y):
            accum_sum[w][h+1]+=accum_sum[w][h]

    # 왼쪽 → 오른쪽
    for w in range(y):
        for h in range(x):
            accum_sum[h+1][w]+=accum_sum[h][w]

    for i in range(x):
        for j in range(y):
            result=board[i][j]+accum_sum[i][j]
            if result > 0 :
                answer+=1

    return answer

print(solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]],
               [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]))

print(solution([[1,2,3],[4,5,6],[7,8,9]],[[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]))



''' 2차원 → 1차원으로 바꿔서
import itertools

def solution(board, skill):
    answer = 0
    row = len(board[1])
    new_board=list(itertools.chain(*board))

    for type_skill,r1,r2,c1,c2,degree in skill:
        start_point=(r1*row)+r2
        end_point=(c1*row)+c2
        for i in range(start_point,end_point+1):
            if type_skill==1:
                new_board[i]-=degree
            else:
                new_board[i]+=degree

    for i in range(0,len(new_board)):
        if new_board[i]>0:
            answer+=1

    return answer
'''