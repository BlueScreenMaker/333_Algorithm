import sys

case=int(sys.stdin.readline())

for i in range(case):
    answer=set()
    A_size=int(sys.stdin.readline())
    A_list=list(map(int,sys.stdin.readline().split()))

    B_size=int(sys.stdin.readline())
    B_list=list(map(int,sys.stdin.readline().split()))

    C_size=int(sys.stdin.readline())
    C_list=list(map(int,sys.stdin.readline().split()))


    for x in range(A_size):
        total=A_list[x]
        for y in range(B_size):
            total+=B_list[y]
            for z in range(C_size):
                total+=C_list[z]
                change=str(total)
                flag=True

                for h in change:
                    if h!='5' and h!='8':
                        flag=False

                if flag:
                    answer.add(total)

                total-=C_list[z]
            total-=B_list[y]

    print(len(answer))