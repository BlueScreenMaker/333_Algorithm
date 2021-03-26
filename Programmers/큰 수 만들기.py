import itertools

def solution(number, k):
    num_list=[]
    for i in number:
        while num_list:
            if i>num_list[-1]:
                if(k>0):
                    num_list.pop()
                    k-=1
                else:
                    break
            else:
                break
        num_list.append(i)
        print(num_list)
    if k>0:
        for i in range(k):
            num_list.pop()

    ans="".join(num_list)
    return ans
print(solution("4177252841",7))


# def solution(number, k):
#     num_list=list(number)
#     length=len(number)
#     combination=[]
#     temp=list(map(''.join, itertools.combinations(num_list,length-k)))
#     combination.extend(temp)
#     answer = max(combination)
#     return answer

