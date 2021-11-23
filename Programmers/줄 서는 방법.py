import math

def solution(n, k):
    answer = []
    number_list=[i for i  in range(1,n+1)]

    while n!=0:
        check=math.factorial(n-1)
        index=(k-1)//check
        k = k % check
        answer.append(number_list.pop(index))
        n-=1
    return answer

print(solution(3,5))