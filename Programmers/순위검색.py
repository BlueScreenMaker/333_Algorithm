import itertools

def solution(info, query):
    answer = []

    info_dic={}

    for i in info:
        x=i.split()
        info_key=x[:-1] # java backend junior pizza
        info_value=int(x[-1]) # 150
        for j in range(5):
            for c in itertools.combinations(info_key,j):
                temp_key=''.join(c) #javabackendpizza
                if temp_key in info_dic:
                    info_dic[temp_key].append(info_value)
                else:
                    info_dic[temp_key]=[info_value]
                    #temp_key값이 중복인 점수가 생길 수 있으므로 리스트 형태로 저장

    for key in info_dic.keys():
        info_dic[key].sort() #key관련 value값 정렬

    for qu in query:
        qu=qu.replace(" and "," ",3)
        q=qu.split(' ')
        q_score=int(q[-1])
        q_query=q[:-1]

        while '-' in q_query:
            q_query.remove('-')

        q_query=''.join(q_query)


        if q_query in info_dic:
            score = info_dic[q_query]
            # count=0
            # for x in score:
            #     if x>=q_score:
            #         count+=1
            # answer.append(count)
            if len(score)>0:
                start,end=0,len(score)
                while start<end:
                    mid=(start+end)//2
                    if score[mid]>=q_score:
                        end=mid
                    else:
                        start=mid+1
                answer.append(len(score)-start)
                # 딕셔너리에서 점수값리스트 불러오고
                # 해당 리스트를 이분탐색
                # 점수가 높으면 만사 오케이니까 큰 지점 찾으면 거기 기준으로 오른쪽값만 봄
        else:
            answer.append(0)

    return answer

print(solution(["java backend junior pizza 150","python frontend senior chicken 210",
                "python frontend senior chicken 150",
                "cpp backend senior pizza 260",
                "java backend junior chicken 80","python backend senior chicken 50"],

               ["java and backend and junior and pizza 100",
                "python and frontend and senior and chicken 200",
                "cpp and - and senior and pizza 250",
                "- and backend and senior and - 150",
                "- and - and - and chicken 100",
                "- and - and - and - 150"]))