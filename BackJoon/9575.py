import sys

# 2
# 6
# 100 1 10 100 1 1
# 7
# 3 53 53 53 53 53 53
# 6
# 4 54 4 54 4 54
# 1
# 47
# 1
# 500
# 1
# 33

case=int(sys.stdin.readline())

for i in range(case):
    count=0
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
                    count+=1

    print(count)