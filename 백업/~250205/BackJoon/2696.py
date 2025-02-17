import sys
import heapq

def calulate_median(count, numbers):
    left_heap = []
    right_heap = []
    for i in range(count):
        if len(left_heap) == len(right_heap):
            heapq.heappush(left_heap, -numbers[i])
        else:
            heapq.heappush(right_heap, numbers[i])

        if right_heap and -(left_heap[0]) > right_heap[0]:
            min_value = heapq.heappop(right_heap)
            max_value = -(heapq.heappop(left_heap))
            heapq.heappush(right_heap, max_value)
            heapq.heappush(left_heap, -min_value)

        if (i + 1) % 2 == 1:
            print(-left_heap[0], end=" ")
    print()

T = int(sys.stdin.readline())
for _ in range(T):
    M = int(sys.stdin.readline())
    nums = list(map(int, sys.stdin.readline().split()))

    if M > 10:
        routine = M // 10
        for _ in range(routine):
            temp = list(map(int, sys.stdin.readline().split()))
            nums += temp
    print((M//2) + 1)
    calulate_median(M, nums)


