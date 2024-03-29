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
    # key: value
    # 방번호 : 다음 최대 방번호
    # 1: 2 / 3: 4 / 4: 5
    for c_idx in room_number:
        visited = [c_idx]
        # visited = [1]
        while c_idx in room:
            # c_idx = 1
            c_idx = room[c_idx]
            # 30: c_idx = room[1] = 2
            # c_idx = 2
            visited.append(c_idx)
            # visited = [1,2]
        answer.append(c_idx)
        for i in visited:
            # room[1] = 2 > 3
            # room[2] = 3
            room[i] = c_idx+1
    return answer

print(solution(10, [1, 3, 4, 1, 3, 1]))