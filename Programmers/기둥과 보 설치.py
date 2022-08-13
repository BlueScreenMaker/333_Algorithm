def check(current):
    for x,y,kind in current:
        # 기둥 일 때
        if kind == 0 :
            # 바닥에 있는 경우
            if y == 0 :
                continue
            # ① 보 왼쪽 위에 있는 경우
            elif [x-1, y, 1] in current:
                continue
            # ② 보의 오른쪽 위에 있는 경우
            elif [x, y, 1] in current:
                continue
            # ③ 기둥 위에 있는 경우
            # 설치할 기둥 (5,1) 이미 있는 기둥 (5,0)
            elif [x,y-1,0] in current:
                continue
            else:
               return False
        # 보 일 때
        else:
            # ④ 한 쪽 끝이 기둥 위에 있음
            if [x,y-1,0] in current:
                continue
            # ⑤ 오른쪽 아래 기둥 설치
            elif [x+1,y-1,0] in current:
                continue
            # ⑥ 양 끝 부분이 보와 연결
            elif [x-1,y,1] in current and [x+1,y,1] in current:
                continue
            else:
                return False
    return True

def solution(n, build_frame):
    answer = []
    for build in build_frame:
        x,y,kind,command = build
        if command==1:
            answer.append([x,y,kind])
            if not check(answer):
                answer.remove([x,y,kind])
        else:
            answer.remove([x,y,kind])
            if not check(answer):
                answer.append([x,y,kind])
    answer.sort()
    return answer

print(solution(5,[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))