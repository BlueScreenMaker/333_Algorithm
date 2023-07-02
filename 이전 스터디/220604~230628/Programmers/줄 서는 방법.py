import math

def solution(n, k):
    answer = []
    number_list=[i for i  in range(1,n+1)]

    while n!=0:
        check=math.factorial(n-1)
        index=k//check
        k = k % check
        if k==0:
            index-=1
        answer.append(number_list.pop(index))
        n-=1
    return answer

print(solution(3,5))