import sys

problem=list(map(int, sys.stdin.readline().split()))

count=0

while True:
    if(problem[0]==0 and problem[1]>0):
        problem[1]-=1
        problem[0]+=1

    if(problem[2]==0):
        if(problem[1]==problem[3]):
            if problem[1]>0:
                problem[1]-=1
                problem[2]+=1

        elif problem[1]>problem[3]:
            problem[1]-=1
            problem[2]+=1
        elif problem[1]<problem[3]:
            problem[3]-=1
            problem[2]+=1

    if(problem[4]==0 and problem[3]>0):
        problem[3]-=1
        problem[4]+=1
    if(problem[0]==0 or problem[2]==0 or problem[4]==0):
        break

    count+=1
    problem[0]-=1
    problem[2]-=1
    problem[4]-=1

print(count)