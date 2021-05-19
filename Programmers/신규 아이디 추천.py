import re

def solution(new_id):
    #1단계
    answer = new_id.lower()
    #2단계
    answer=re.sub('[^a-z\d\-\_\.]','',answer)
    #3단계
    answer=re.sub('\.+','.',answer)
    #4단계
    answer=re.sub('^\.|\.$','',answer)
    #5단계
    if not answer:
        answer='a'
    #6단계
    if len(answer)>=16:
        answer=answer[:15]
        if answer[-1]=='.':
            answer=answer[:-1]
    #7단계
    if len(answer)<3:
        answer=answer+answer[-1]*(3-len(answer))

    return answer

print(solution("=.="))