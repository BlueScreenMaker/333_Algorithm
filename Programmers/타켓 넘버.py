answer = 0

def operation(number,count, target, total):
    global answer
    if count>=len(number):
        if total==target:
            answer+=1
        return
    else:
        check=number[count]
        for i in [-1,+1]:
            temp=check*i
            operation(number,count+1,target,total+temp)

def solution(numbers, target):
    global answer
    operation(numbers,0,target,0)
    return answer

print(solution([1, 1, 1, 1, 1],3))