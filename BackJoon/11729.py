def Move_hanoi(n,front,end,middle):
    if n==1:
        return print(front,end,sep=' ')
    Move_hanoi(n-1,front,middle,end)
    print(front,end,sep=' ')
    Move_hanoi(n-1,middle,end,front)

num=int(input())
print((2**num)-1)
Move_hanoi(num,1,3,2)
