# parentheses=list(input())
# stack_list=[]
# Flag=False
# for i in parentheses:
#     if(i=='('):
#         stack_list.append(i)
#     else:
#         if not stack_list:
#             Flag=True
#             print(False)
#             break
#         else:
#             stack_list.pop()
#
# if not stack_list and Flag==False:
#     print(True)

def solution(parentheses):
    answer = True
    stack_list=[]
    for i in parentheses:
        if(i=='('):
            stack_list.append(i)
        else:
            if not stack_list:
                answer=False
                break
            else:
                stack_list.pop()
    if stack_list:
        answer=False
    return answer

print(solution('()))'))