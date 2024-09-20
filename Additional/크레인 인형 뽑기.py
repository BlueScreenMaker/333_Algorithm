# Level 1
def solution(board, moves):
    answer = 0
    length = len(board)
    stack = []
    for move in moves:
        for i in range(length):
            if board[i][move-1]:
                stack.append(board[i][move-1])
                board[i][move-1] = 0
                break
        if len(stack) > 1:
            a = stack.pop()
            b = stack.pop()
            if a == b:
                answer += 2
            else:
                stack.append(b)
                stack.append(a)
    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))