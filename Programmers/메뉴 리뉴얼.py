import itertools
import collections

def solution(orders, course):
    answer = []

    for num in course:
        find=[]
        for menu in orders:
            result=itertools.combinations(menu,num)
            find+=result
            print(find)
        count=collections.Counter(find)
        if count:
            maxCount=max(count.values())
            if maxCount>=2:
                for k,v in count.items():
                    if count[k]==maxCount:
                        answer.append(''.join(k))


    return sorted(answer)

# print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4]))
print(solution(["XYZ", "XWY", "WXA"],[2,3,4]))