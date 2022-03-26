import math
from collections import Counter

def solution(str1, str2):
    candi1=[]
    candi2=[]

    for i in range(0,len(str1)-1):
        if str1[i:i+2].isalpha():
            candi1.append(str1[i:i+2].lower())
    for j in range(0, len(str2)-1):
        if str2[j:j+2].isalpha():
            candi2.append(str2[j:j + 2].lower())

    if len(candi1)==0 and len(candi2)==0:
        return 65536

    A=Counter(candi1)
    B=Counter(candi2)

    intersection = sum((A & B).values())
    union=sum((A | B).values())
    answer=math.trunc((intersection/union)*65536)

    return answer

print(solution("FRANCE","FRENCH"))
# print(solution("aa1+aa2","AAAA12"))
