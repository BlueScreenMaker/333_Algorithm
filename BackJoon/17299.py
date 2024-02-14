import sys
from collections import Counter

N = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split(" ")))

count = Counter(num_list)
result = [-1] * N
stack = [0]

for i in range(1, N):
    while stack and count[num_list[stack[-1]]] < count[num_list[i]]:
        result[stack.pop()] = num_list[i]
    stack.append(i)

print(" ".join(map(str, result)))
'''
시간초과

big_num = {}
sequence = []
for i in range(N):
    check = num_list[i]
    if str(check) not in big_num:
        big_num[str(check)] = 1
        sequence.append(check)
    else:
        big_num[str(check)] += 1

answer = []
while True:
    if num_list:
        value = num_list.pop()
        F = big_num[str(value)]
        pos = sequence.index(value)
        result = -1
        for i in range(0, pos):
            if big_num[str(sequence[i])] > F:
                result = sequence[i]
        answer.append(result)

    else:
        break
print(answer[::-1])
'''