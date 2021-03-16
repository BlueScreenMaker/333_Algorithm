def solution(jobs):
    jobs=sorted(jobs,key=lambda x:x[1])
    time=0
    answer = 0
    length=len(jobs)
    while len(jobs)!=0:
        for i in range (0,len(jobs)):
            if jobs[i][0]<=time:
                time+=jobs[i][1]
                answer+=time-jobs[i][0]
                jobs.pop(i)
                break
            if i==len(jobs)-1:
                time+=1

    return answer // length

print(solution([[0, 3], [1, 9], [2, 6]]))