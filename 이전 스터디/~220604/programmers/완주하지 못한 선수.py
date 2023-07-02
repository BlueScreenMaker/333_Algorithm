# import copy
# def solution(participant, completion):
#     temp=copy.deepcopy(participant)
#     for i in completion:
#         print("i값",i)
#         if (i in participant):
#             temp.remove(i)
#     return "".join(map(str, temp))
#
# print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))


def solution(participant, completion):
    participant.sort()
    completion.sort()
    answer=''
    for i in range(0, len(completion)):
        if(completion[i]!=participant[i]):
            answer=participant[i]
    if(answer==''):
        answer=participant[-1]
    return answer