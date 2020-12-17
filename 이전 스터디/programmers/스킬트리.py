
def solution(skill, skill_trees):
    answer = 0

    for i in range(0,len(skill_trees)):
        point = False
        case=list(skill_trees[i])
        flag=1
        for j in range(0,len(case)):
            if case[j] == skill[flag - 1]:
                flag += 1
                if(flag>=len(skill)):
                    break
            elif case[j] in skill[flag:]:
                point=True
                break
        if point==False:
            # print(skill_trees[i])
            answer+=1
    return answer

print(solution("CBD",["BACDE","CBADF", "AECB", "BDA"]))
# print(solution("CBD",["CBADF"]))
