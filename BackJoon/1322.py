import sys

X, K = map(int, sys.stdin.readline().split())

bin_x = format(X, "b")
x_64 = bin_x[::-1]
x_length = len(bin_x)

for a in range(64 - x_length + 1):
    x_64 += "0"

pos = []
for b in range(65):
    if x_64[b] == "0":
        pos.append(b)

bin_k = format(K, "b")
k_64 = bin_k[::-1]
k_length = len(bin_k)
for a in range(64 - k_length + 1):
    k_64 += "0"

result = [0 for _ in range(65)]
for idx in range(65):
    if k_64[idx] == "1":
        result[pos[idx]] = 1

convert = ''.join(map(str, result))
answer = int(convert[::-1], 2)
print(answer)