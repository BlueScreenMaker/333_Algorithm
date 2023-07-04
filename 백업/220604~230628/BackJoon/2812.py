import sys

N,K=map(int,sys.stdin.readline().split())

l=N-K

number=list(sys.stdin.readline())

number=number[:-1]

number=list(map(int,number))


result=[]

for i in range(N):
    while K>0 and result:
        if result[-1]<number[i]:
            result.pop()
            K-=1
        else:
            break
    result.append(number[i])

for i in range(l):
    print(result[i],end="")
