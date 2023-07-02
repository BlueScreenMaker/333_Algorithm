def solution(scores):
    answer = 0
    ho_score = scores[0]
    scores.sort(key=lambda x: (-x[0], x[1]))

    min_eval = -1
    for i in range(0,len(scores)):
        del_value = False

        if min_eval < scores[i][1]:
            min_eval = scores[i][1]
            print(min_eval)

        elif min_eval > scores[i][1]:
            del_value = True

        if del_value:
            if scores[i][0] == ho_score[0] and scores[i][1] == ho_score[1]:
                return -1
            continue

        if sum(scores[i]) > sum(ho_score):
            answer += 1

    return answer + 1

print(solution([[2,2],[1,4],[3,2],[3,2],[2,1]]))