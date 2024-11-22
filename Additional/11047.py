import sys

N, K = map(int,sys.stdin.readline().split())

coins = []
for _ in range(N):
    coins.append(int(sys.stdin.readline()))

count = 0
for i in range(N-1, -1, -1):
    if K == 0:
        break
    else:
        if coins[i] <= K:
            temp = K // coins[i]
            count += temp
            K -= temp * coins[i]

print(count)
