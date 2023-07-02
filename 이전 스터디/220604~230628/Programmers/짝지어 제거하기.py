def solution(s):
    check=[]
    for i in s:
        if not check:
            check.append(i)
            continue
        flag=check[-1]
        if flag==i:
            check.pop()
        else:
            check.append(i)

    if check:
        answer=0
    else:
        answer=1

    return answer

# 시초 풀이
# def solution(s):
#     while True:
#         flag=True
#         for i in range(0,len(s)-1):
#             if s[i]==s[i+1]:
#                 flag=False
#                 s=s[0:i]+s[i+2:]
#                 break
#         if flag:
#             break
#     if s:
#         answer=0
#     else:
#         answer=1
#     return answer


print(solution("baabaa"))
print(solution("cdcd"))