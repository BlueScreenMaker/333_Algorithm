import sys

N = int(sys.stdin.readline())
port = list(map(int, sys.stdin.readline().split(' ')))
count = []

for num in port:
    if not count or count[-1] < num:
        count.append(num)
    else:
        start = 0
        end = len(count)
        while start < end:
            mid = (start + end) // 2
            if count[mid] <= num:
                start = mid + 1
            else:
                end = mid
        count[start] = num

print(len(count))