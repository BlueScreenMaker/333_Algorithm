import sys

N=int(sys.stdin.readline())

stack=list(sys.stdin.readline())
stack=stack[:-1] #개행문자 빼고
stack=stack[::-1] #뒤집어줍니다.


woman=0
man=0

while stack:
    check=stack.pop()
    if check=='W':
        if abs((woman+1)-man)<=N:
            woman+=1
        elif stack and abs((woman+1)-man)>N:
            next=stack.pop()
            if next=='M':
                if abs((man+1)-woman)<=N:
                    man+=1
                    stack.append(check)
            else:
                break
        else:
            break
    else:
        if abs((man+1)-woman)<=N:
            man+=1
        elif stack and abs((man+1)-woman)>N:
            next=stack.pop()
            if next=='W':
                if abs((woman+1)-man)<=N:
                    woman+=1
                    stack.append(check)
            else:
                break
        else:
            break

print(woman+man)

