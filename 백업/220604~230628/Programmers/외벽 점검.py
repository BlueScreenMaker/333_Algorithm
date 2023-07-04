from itertools import permutations

def solution(n, weak, dist):
    answer = len(dist)+1
    length = len(weak)
    for i in range(length):
        weak.append(weak[i]+n)

    for idx in range(length):
        for jobs in list(permutations(dist, len(dist))):
            friend=1
            # 선택된 친구가 움직일 수 있는 총 거리
            pos = weak[idx] + jobs[friend-1]
            # 모든 취약 지점 순회
            for check in range(idx, idx+length):
                if pos < weak[check]:
                    friend+=1
                    if friend > len(dist):
                        break
                    pos = weak[check]+jobs[friend-1]
            answer = min(answer,friend)
    if answer > len(dist):
        return -1
    return answer

print(solution(12, [1,5,6,10],[1,2,3,4]))