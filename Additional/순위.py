def solution(n, results):
    data = [[0 for _ in range(n+1)] for _ in range(n+1)]

    for check in results:
        a,b = check
        data[a][b] = 1 # 이김
        data[b][a] = -1 # 짐

    for i in range(1, n+1):
        for j in range(1, n+1):
            for k in range(1, n+1):
                if data[i][k] == data[k][j] == 1:
                    data[i][j] = 1
                    data[j][i] = -1
                if data[i][k] == data[k][j] == -1:
                    data[i][j] = -1
                    data[j][i] = 1

    answer = 0
    for a in range(1, n+1):
        count = 0
        for b in range(1, n+1):
            if data[a][b]:
                count+=1
        if count == n-1:
            answer +=1

    return answer

print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))