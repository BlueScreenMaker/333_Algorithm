import sys

X,Y=map(int, sys.stdin.readline().split())

#Z=math.floor(100*Y/X) =>내림
#z=math.trunc(100*Y/X) =>내림
# floor는 음수를 내림 시 -1 이 더 더해짐. -3.14가 -4가 됨
# trunc는 음수 내림시 소수점만 버림, -3.14가 -3이 됨
Z=100*Y//X


answer=0
if Z>=99:
    answer=-1
else:
    left=1
    right=10000000000
    while left<=right:
        mid=(left+right)//2
        new_percent=100*(Y+mid)//(X+mid)
        if new_percent==Z:
            left=mid+1
        else:
            right=mid-1
            answer=mid

print(answer)

# answer=-1
#
# if(Z<99):
#     up=100*Y - X(Z+1)
#     down=Z-99
#     answer=up//down
#
#
# print(answer)