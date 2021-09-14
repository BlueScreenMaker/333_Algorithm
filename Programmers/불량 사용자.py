import itertools
import re

def solution(user_id, banned_id):
    answer=[]
    n=len(banned_id)
    candidate=itertools.permutations(user_id,n)

    for i in range(n):
        banned_id[i]=banned_id[i].replace('*','.')

    for check in candidate:
        count=0
        for j in range(n):
            if not re.match(banned_id[j],check[j]) or len(banned_id[j])!=len(check[j]):
                break
            else:
                count+=1
        if count==n:
            temp=sorted(check)
            print(temp)
            if temp not in answer:
                answer.append(temp)

    return len(answer)


print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "*rodo", "******", "******"]))