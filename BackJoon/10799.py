stick=input()
stack=[]
ans=0
stack.append(stick[0])
for i in range(1,len(stick)):
    if stick[i] =='(':
        stack.append(stick[i])
    else:
        if(stick[i-1]=='('):
            stack.pop()
            ans+=len(stack)
        else:
            stack.pop()
            ans+=1

print(ans)
