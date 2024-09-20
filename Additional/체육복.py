# Level 1
def solution(n, lost, reserve):
    answer = n - len(lost)

    lost.sort()
    reserve.sort()

    for i in range(len(lost)):
        for j in range(len(reserve)):
            if lost[i] == reserve[j]:
                lost[i] = -1
                reserve[j] = -1
                answer += 1
                break # 잃어버린 사람 == 여분 찾으면 더는 찾을 필요 없으니까.

    # 체육복을 빌려 줄 수 있는 상황인가?
    for i in range(len(lost)):
        for j in range(len(reserve)):
            if lost[i]-1 == reserve[j] or lost[i]+1 == reserve[j]:
                answer += 1
                reserve[j] = -1
                break # 더 검색할 필요 없음

    return answer

print(solution(5, [2, 4],[1, 3, 5]))
print(solution(5,[2, 4],[3]))