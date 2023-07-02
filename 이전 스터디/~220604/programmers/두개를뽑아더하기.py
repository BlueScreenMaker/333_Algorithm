def solution(numbers):
    num_list=numbers
    answer = []
    for index, value in enumerate(num_list):
        for j in range(index+1,len(num_list)):
            print("i",index,"J",j)
            temp=value+num_list[j]
            if not temp in answer:
                answer.append(temp)
    right=sorted(answer)
    return right


print(solution([2,1,3,4,1]))