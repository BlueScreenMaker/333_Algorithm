def solution(s):
    number_list=list(map(int,s.split()))
    sort_number=sorted(number_list)

    answer=str(sort_number[0])+" "+str(sort_number[-1])
    return answer


print(solution("-1 -2 -3 -4"))