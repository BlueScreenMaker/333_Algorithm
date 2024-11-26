import itertools
import re

def solution(user_id, banned_id):
    answer = []
    n = len(banned_id)
    candidate = itertools.permutations(user_id, n)

    for i in range(n):
        # . = 한 문자 대체
        banned_id[i] = banned_id[i].replace("*", ".")

    for cadi in candidate:
        count = 0
        for i in range(n):
            if not re.match(banned_id[i], cadi[i]) or len(banned_id[i]) != len(cadi[i]):
                break
            else:
                count += 1
        if count == n:
            temp = sorted(cadi)
            if temp not in answer:
                answer.append(temp)

    return len(answer)

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))