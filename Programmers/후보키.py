from itertools import combinations

def solution(relation):
    attribute=len(relation)
    col=len(relation[0])
    candi = []
    for i in range(1, col + 1):
        candi.extend(combinations(range(col), i))
    unique=[]
    # [(0,), (1,), (2,), (3,), (0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3), (0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3), (0, 1, 2, 3)]
    for i in candi:
        temp=[]
        for item in relation:
            temp.extend([tuple([item[key] for key in i])])
        if len(set(temp))==attribute:
            flag=True
            for z in unique:
                if set(z).issubset(set(i)):
                    flag=False
                    break
            if flag:
                unique.append(i)

    return len(unique)

print(solution([["100","ryan","music","2"],
                ["200","apeach","math","2"],
                ["300","tube","computer","3"],
                ["400","con","computer","4"],
                ["500","muzi","music","3"],
                ["600","apeach","music","2"]]))