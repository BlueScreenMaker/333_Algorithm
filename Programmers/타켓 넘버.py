def operation(number,count, target, total):
    if count>len(number):
        if total==target:
            return True
        else:
            return False
    else:
        check=number.pop(0)
        for i in [-1,+1]:
            temp=check*i
            total+=temp
            print(total)
            operation(number,count+1,target,total)

def solution(numbers, target):
    visited = [False * len(numbers)]
    print(operation(numbers,0,target,0,visited))
    answer = 0
    return answer

print(solution([1, 1, 1, 1, 1],3))