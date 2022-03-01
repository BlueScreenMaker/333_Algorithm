def solution(progresses, speeds):
    answer = []
    count=0
    while progresses:

        for i in range(len(progresses)):
            progresses[i]+=speeds[i]
        print(progresses)
        if progresses[0]>=100:
            while progresses:
                if progresses[0]>=100:
                    count+=1
                    progresses.pop(0)
                    speeds.pop(0)
                else:
                    answer.append(count)
                    count=0
                    break

    answer.append(count)
    return answer

# print(solution([93, 30, 55],[1, 30, 5]))
# print(solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1]))
# print(solution([20, 99, 93, 30, 55, 10], [5, 10, 1, 1, 30, 5]))
# print(solution([96, 99, 98, 97], [1, 1, 1, 1]))
print(solution([40, 93, 30, 55, 60, 65], [60, 1, 30, 5, 10, 7]))