import itertools

def solution(info, query):
    answer = []

    info_dic={}

    for x in info:
        li=x.split()
        info_key=li[:-1]
        info_value=int(li[-1])
        for i in range(5):
            for c in itertools.combinations(info_key,i):
                tmp_key=''.join(c)
                if tmp_key in info_dic:
                    info_dic[tmp_key].append(info_value)
                else:
                    info_dic[tmp_key]=[info_value]

    for key in info_dic.keys():
        info_dic[key].sort()

    for qu in query:
        q=qu.split(' ')
        q_score=int(q[-1])
        q_query=q[:-1]

        while 'and' in q_query:
            q_query.remove('and')

        while '-' in q_query:
            q_query.remove('-')

        q_query=''.join(q_query)

        if q_query in info_dic:
            score=info_dic[q_query]
            if len(score)>0:
                start,end=0,len(score)
                while start<end:
                    mid=(start+end)//2
                    if score[mid]>=q_score:
                        end=mid
                    else:
                        start=mid+1
                answer.append(len(score)-start)
        else:
            answer.append(0)


    return answer

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
               ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))