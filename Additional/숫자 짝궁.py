# Level 1
def solution(X, Y):
    answer = ''
    x_intersection = [0 for _ in range(10)]
    y_intersection = [0 for _ in range(10)]
    for x in X:
        x_intersection[int(x)] += 1
    for y in Y:
        y_intersection[int(y)] += 1

    for i in range(9, 0, -1):
        if x_intersection[i] and y_intersection[i]:
            answer += min(x_intersection[i], y_intersection[i]) * str(i)

    if x_intersection[0] and y_intersection[0]:
        if not answer:
            answer = "0"
        else:
            # 앞에 숫자가 있ㄱ 0이 여러개 있는 경우
            answer += min(x_intersection[0], y_intersection[0]) * str(0)
    return answer if  answer else "-1"

print(solution("100","2345"))
print(solution("100","203045"))
print(solution("100","123450"))
print(solution("12321","42531"))
print(solution("5525","1255"))