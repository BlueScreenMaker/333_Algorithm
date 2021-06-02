def solution(numbers):
    answer = []
    for i in numbers:
        if i%2==0:
            answer.append(i+1)
        else:
            bin_num=format(i,'b')
            print(bin_num)
    return answer

print(solution({2,7}))