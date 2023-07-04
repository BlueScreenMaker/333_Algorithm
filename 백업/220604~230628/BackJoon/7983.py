import sys

N=int(sys.stdin.readline())

time=[]
for i in range(N):
    time.append(list(map(int,sys.stdin.readline().split())))

time=sorted(time, key=lambda x:x[1],reverse=True)

point=time[0][1]-time[0][0]

# 하루에 과제 2개도 못한다니 그런 마음으로 놀겠다니 안일한 자식
# 결론, 첫번째 과제 시행하는 날짜가 point

for j in range(1,N):
    if point>=time[j][1]:
        point=time[j][1]-time[j][0]
    else:
        point=point-time[j][0]

print(point)