import itertools

def solution(nums):
    answer = set()
    input_list=list(map(str, nums))
    result_list=[]
    for i in range(1,len(nums)+1):
        temp=list(map(''.join, itertools.permutations(input_list, i)))
        result_list.extend(temp)
    result_list=set(map(int, result_list))
    for a in result_list:
        flag=False
        if(a>1):
            for b in range(2,a):
                if(a%b==0):
                    flag=True
                    break
            if(flag==False):
                answer.add(a)
    return len(answer)

print(solution("011"))



#     c = combinations(nums, i)
    #     result.extend(c)
    #     print(c)
    # for a in result:
    #     for i in range(2,len(result[-1]))