import sys

K=int(sys.stdin.readline())

sign=list(map(str,sys.stdin.readline().split()))
visited=[False] * 10

min_str=""
max_str=""

def check(num1,num2,equals):
    if equals=='<':
        return num1<num2
    else:
        return num1>num2

def solution(count, s):
    global min_str,max_str

    if count==K+1:
        if not len(min_str):
            min_str=s
        else:
            max_str=s
        return
    for i in range(10):
        if not visited[i]:
            if count==0 or check(s[-1],str(i),sign[count-1]):
                visited[i]=True
                solution(count+1,s+str(i))
                visited[i]=False

solution(0,"")
print(max_str)
print(min_str)