def solution(s):
    answer = 1

    for i in range(len(s)):
        for j in range(i + 1, len(s)+1):
            temp = s[i:j]
            if temp == temp[::-1]:
                answer = max(answer, len(temp))

    return answer
print(solution("abacde"))


# def solution(s):
#     answer=0
#
#     length=len(s)
#
#     start=0
#     end=length-1
#
#     while start<=end:
#         if s[start]==s[end]:
#             start+=1
#             end-=1
#         else:
#             end-=1
#
#     compare1=s[:start]
#     compare2=s[start:start+len(compare1)]
#
#     if compare1==compare2[::-1]:
#         answer+=start*2
#     else:
#         answer+=start+(start-1)
#     return answer

# print(solution("ABCCBA"))
