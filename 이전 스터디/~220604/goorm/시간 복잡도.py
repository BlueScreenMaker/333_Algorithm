import math
N=int(input())
count=0
square=1

while True:
    count+=N//(5 ** square)
    if (5 ** square) <= N:
        square += 1
    else:
        break


print(count)
# for i in range(1,N+1):
#     number=math.factorial(i)
#     print(number)



