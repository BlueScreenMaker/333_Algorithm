tags=[]

while True:
    string=input()
    if (string=="#"):
        break
    else:
        tags.append(string)


for s in tags:
    flag=0
    stack=[]
    for j in range(len(s)):
        if s[j]=="<":
            flag=j+1
        elif s[j]==">":
            temp=s[flag:j]
            if "/" in temp:
                if temp[:-2]=="/>":
                    continue
                else:
                    if stack:
                        check=stack.pop()
                        if check!=temp[1:]:
                            stack.append(check)
                    else:
                        stack.append(temp)
                        break
            else:
                if temp.startswith('a'):
                    stack.append(temp[0])
                else:
                    stack.append(temp)

    if not stack:
        print("legal")
    else:
        print("illegal")





