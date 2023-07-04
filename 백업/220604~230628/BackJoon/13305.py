import sys

N=int(sys.stdin.readline())

distance=list(map(int,sys.stdin.readline().split()))
oil_price=list(map(int,sys.stdin.readline().split()))

total=0
row_price=oil_price[0]
for i in range(0,N-1):
    if oil_price[i]<row_price:
        row_price=oil_price[i]
    total+=row_price*distance[i]

print(total)
