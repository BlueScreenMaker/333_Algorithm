def solution(n, m, x, y, queries):
    answer = 0
    x_min, x_max, y_min, y_max = x, x, y, y

    for i in range(len(queries)-1, -1, -1):
        way, dist = queries[i]

        if way == 0: # 실제: 좌측 이동 / 거꾸로: 우측 이동
            y_max += dist
            if y_max > m-1: # 우측의 범위 밖으로 이동시
                y_max = m-1
            if y_min != 0: # 왼쪽 벽이 아닌 경우, 왼쪽 지역 축소
                y_min += dist

        elif way == 1: # 실제: 우측 이동 / 거꾸로: 좌측 이동
            y_min -= dist
            if y_min < 0:
                y_min = 0 # 좌측 영역 줄이기
            if y_max != m-1:
                y_max -= dist # 우측이 벽이 아닌 경우 우측 지역 축소

        elif way == 2: #실제: 위로 이동 / 거꾸로: 아래로 이동
            x_max += dist
            if x_max > n-1:
                x_max = n-1
            if x_min != 0:
                x_min += dist

        else: #실제: 아래 이동 / 거꾸로: 위에 이동
            x_min -= dist
            if x_min < 0:
                x_min = 0
            if x_max != n-1:
                x_max -= dist
        if y_min > m-1 or y_max < 0 or x_min > n-1 or x_max < 0 :
            return answer
    else:
        answer = (y_max - y_min + 1) * (x_max - x_min +1)

    return answer
