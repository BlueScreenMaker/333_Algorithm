# Level 1
import re
# def solution(ingredient):
#     answer = 0
#     check = "1231"
#     ingredient = ''.join(map(str, ingredient))
#     while True:
#         match = re.search(check, ingredient)
#         if match:
#             answer += 1
#             ingredient = re.sub(check, '', ingredient)
#         else:
#             break
#     return answer

def solution(ingredient):
    answer = 0
    stack = []
    for i in ingredient:
        stack.append(i)
        if stack[-4:] == [1,2,3,1]:
            answer += 1
            for k in range(4):
                stack.pop()
    return answer

print(solution([2, 1, 1, 2, 3, 1, 2, 3, 1]))
print(solution([[1, 3, 2, 1, 2, 1, 3, 1, 2]]))