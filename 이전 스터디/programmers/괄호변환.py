def solution(p):
    answer = p
    if p=='':
        answer=''
    else:
        stack_list=list(answer)
        parentheses_list=[]
        parentheses_list.append(stack_list[0])
        for index in range(1,len(stack_list)):
            if stack_list[0]==stack_list[index]:
                parentheses_list.append(stack_list[index])
            else:
                parentheses_list.pop()
                if not parentheses_list:
                    break

        u = "".join(map(str, stack_list[:index + 1]))
        v = "".join(map(str, stack_list[index + 1:]))
        if rightParenthes(u) == True:
            u += solution(v)
            return u
        else:
            temp = '('
            temp += solution(v)
            temp += ')'
            temp += reverse(u[1:-1])
            return temp


    return answer

def reverse(u):
    temp_list=[]
    for index, value in enumerate(u):
        if value=='(':
            temp_list.append(')')
        else:
            temp_list.append('(')
    return  "".join(map(str, temp_list))

def rightParenthes(parentheses):
    answer=True
    stack_list=[]
    for i in parentheses:
        if (i == '('):
            stack_list.append(i)
        else:
            if not stack_list:
                answer = False
                break
            else:
                stack_list.pop()
    if stack_list:
        answer = False
    return answer

print(solution(')('))