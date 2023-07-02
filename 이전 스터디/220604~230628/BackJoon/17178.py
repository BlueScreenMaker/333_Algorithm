import sys

N=int(sys.stdin.readline())

ticket=[]
for i in range(N):
    number=list(sys.stdin.readline().split())
    for j in number:
        a1=ord(j[:1])*1000
        a2=int(j[2:])
        ticket.append(a1+a2)

ticket_sort=sorted(ticket, reverse=True)

ticket=ticket[::-1]

stack=[]

while True:
    if ticket_sort:
        point=ticket_sort[-1]
        if ticket:
            if point==ticket[-1]:
                ticket.pop()
                ticket_sort.pop()
            else:
                if stack:
                    if point==stack[-1]:
                        stack.pop()
                        ticket_sort.pop()
                    else:
                        stack.append(ticket.pop())
                else:
                    stack.append(ticket.pop())
        else:
            if stack:
                if point==stack[-1]:
                    stack.pop()
                    ticket_sort.pop()
                else:
                    break
            else:
                break
    else:
        break

if not (stack and ticket_sort):
    print("GOOD")
else:
    print("BAD")


''' 문자열 치환 안하고 그냥 쌩으로

N=int(sys.stdin.readline())

ticket=[]
for i in range(N):
    a,b,c,d,e=sys.stdin.readline().split()
    a1=a[:1] 
    a2=int(a[2:]) 
    ticket.append([a1,a2])
    b1=b[:1]
    b2=int(b[2:])
    ticket.append([b1,b2])
    c1=c[:1]
    c2=int(c[2:])
    ticket.append([c1,c2])
    d1=d[:1]
    d2=int(d[2:])
    ticket.append([d1,d2])
    e1=e[:1]
    e2=int(e[2:])
    ticket.append([e1,e2])

ticket_sort=sorted(ticket,key=lambda x:(x[0],x[1]),reverse=True)

stack=[]

ticket=ticket[::-1]

while True:
    if ticket_sort:
        point_a, point_n=ticket_sort[-1]
        if ticket:
            t1,t2=ticket[-1]
            if point_a==t1 and point_n==t2:
                ticket.pop()
                ticket_sort.pop()
            else:
                if stack:
                    s1, s2=stack[-1]
                    if point_a==s1 and point_n==s2:
                        stack.pop()
                        ticket_sort.pop()
                    else:
                        stack.append(ticket.pop())
                else:
                    stack.append(ticket.pop())
        else:
            if stack:
                ss1,ss2=stack[-1]
                if point_a==ss1 and point_n==ss2:
                    stack.pop()
                    ticket_sort.pop()
                else:
                    break
            else:
                break
    else:
        break

if not (stack and ticket_sort):
    print("GOOD")
else:
    print("BAD")
'''