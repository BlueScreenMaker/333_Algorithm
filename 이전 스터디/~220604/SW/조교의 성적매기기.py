T=int(input())
for _ in range(0,T):
    N, K = map(int, input().split())
    level = ['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0']
    grade=[]
    for i in range(0,N):
        middle, final, task=map(int, input().split())
        total=(middle*0.35)+(final*0.45)+(task*0.2)
        grade.append([round(total,2),i+1])
    grade=sorted(grade, reverse=True)
    for index, value in enumerate(grade):
        if (K==value[1]):
            N=N/10
            index=int(index/N)
            print(f"#{_+1} {level[index]}")
            break

# position=K/(N/10)