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
    stop=False
    for j in range(len(s)):
        if s[j]=="<":
            flag=j+1
        elif s[j]==">":
            if s[j-1]=='/':
                continue
            else:
                temp=s[flag:j]
                if temp[0]=="/":
                    if stack:
                        check=stack.pop()
                        if check!=temp[1:]:
                            stop=True
                    else:
                        stop=True

                else:
                    add=temp.split(" ")[0]
                    stack.append(add)


    if not stack:
        if stop:
            print("illegal")
        else:
            print("legal")
    else:
        print("illegal")
