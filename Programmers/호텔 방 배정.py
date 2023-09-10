# 효율성 없는 풀이
def no_efficiency(k, room_number):
    answer = []
    room = [False for _ in range(k+1)]
    for custom_idx in room_number:
        if not room[custom_idx]:
            answer.append(custom_idx)
            room[custom_idx] = True
        else:
            flag = custom_idx + 1
            while flag <= k:
                if not room[flag]:
                    answer.append(flag)
                    room[flag] = True
                    break
                flag += 1
    return answer

def solution(k, room_number):
    answer = []
    room = {}
    for c_idx in room_number:
        origin = c_idx
        visited = [c_idx]
        # 이미 배정된 방인 경우
        while c_idx in room:
            c_idx = room[c_idx]
            visited.append(c_idx)
            # 갱신된 c_idx가 여전히 방에 있는 경우, 계속 업데이트
        # 배정 되지 않는 방인 경우
        answer.append(c_idx)
        for i in visited:
            # 다음 빈 방을 dict에 넣음
            room[i] = c_idx+1
    return answer

print(solution(10, [1, 3, 4, 1, 3, 1]))