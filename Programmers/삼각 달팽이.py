from itertools import chain
def solution(n):
    num = [[0 for _ in range(n)] for _ in range(n)]
    x,y = -1, 0
    number = 1
    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0:
                x += 1
            elif i % 3 == 1:
                y += 1
            elif i % 3 == 2:
                x -= 1; y -= 1
            num[x][y] = number
            number += 1
    ans = [i for i in chain(*num) if i != 0]
    return ans

print(solution(5))