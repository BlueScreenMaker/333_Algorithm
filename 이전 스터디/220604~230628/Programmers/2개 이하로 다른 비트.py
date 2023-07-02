def solution(numbers):
    answer = []
    for i in numbers:
        if i%2==0:
            answer.append(i+1)
        else:
            bin_num=str(format(i,'b'))
            point=bin_num.rfind('01')
            if point==-1:
                bin_num='10'+bin_num[1:]
                print(bin_num)
                answer.append(int(bin_num,2))
            else:
                bin_num=bin_num[:point]+'10'+bin_num[point+2:]
                # index 값 범위를 넘어가면 빈값출력
                answer.append(int(bin_num,2))
    return answer

print(solution({2,45}))