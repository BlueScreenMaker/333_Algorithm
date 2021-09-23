import sys

R,C=map(int,sys.stdin.readline().split())

num_list=[]

for a in range(R):
    num_list.append(list(sys.stdin.readline().rstrip()))

start=0
end=R

count=0

while start<=end:
    mid=(start+end)//2
    result = []
    for i in range(C):
        temp=""
        flag = False
        for j in range(mid,R):
            temp+=num_list[j][i]
        if temp in result:
            flag=True
            break
        else:
            result.append(temp)
    if flag:
        end=mid-1
        count = mid-1
    else:
        start=mid+1

print(count)