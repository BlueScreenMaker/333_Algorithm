length, total = map(int, input().split())

fish = [0] + list(map(int, input().split()))
count = 0

for a in range(1, length + 1):
    fish[a] += fish[a - 1]

flag = 0
for i in range(1, length + 1):
    for j in range(flag, i):
        if (fish[i] >= total):
            temp = fish[i] - fish[j]
            flag = j
            if (total == temp):
                count += 1
                break
            elif (total > temp):
                flag -= 1
                break
        else:
            break

print(count)