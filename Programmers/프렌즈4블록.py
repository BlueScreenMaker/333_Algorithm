def solution(m, n, board):
    answer = 0
    block=[[v for v in z] for z in board]

    flag=True
    while flag:
        flag = False
        same_block = [[False for _ in range(0,n)] for _ in range(0,m)]
        # print(same_block)
        for i in range(0,m-1):
            for j in range(0,n-1):
                if block[i][j]!='0' and block[i][j]==block[i][j+1]==block[i+1][j]==block[i+1][j+1]:
                    same_block[i][j]=True
                    same_block[i][j+1]=True
                    same_block[i+1][j]=True
                    same_block[i+1][j+1]=True
                    flag=True

        for a in range(0,m):
            for b in range(0,n):
                if same_block[a][b]==True:
                    block[a][b]='0'
                    answer+=1
        # print(block)

        for y in range(0,n):
            count=0
            for x in range(m-1,-1,-1):
                # print(x,y)
                if block[x][y]=='0':
                    count+=1
                elif count>0:
                    temp=x+count
                    block[temp][y]=block[x][y]
                    block[x][y]='0'



    return answer


print(solution(4,5,["CCBDE", "AAADE", "AAABF", "CCBBF"]))