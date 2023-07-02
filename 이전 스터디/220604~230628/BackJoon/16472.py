import sys

N=int(sys.stdin.readline())

s=list(sys.stdin.readline().rstrip())

start=0
answer=0

kind={}

for end in range(len(s)):
    if s[end] not in kind:
        kind[s[end]]=1
    else:
        kind[s[end]]+=1
    while len(kind)>N:
        kind[s[start]]-=1
        if kind[s[start]]==0:
            del kind[s[start]]
        start+=1
    answer=max(answer,end-start+1)
print(answer)
