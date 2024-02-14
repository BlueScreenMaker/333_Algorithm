import sys
import heapq

# 왜 최대값을 먼저 처리하면 안될까..?
N, K = map(int, sys.stdin.readline().split(" "))
jewel = []
for _ in range(N):
    M, V= map(int, sys.stdin.readline().split(" "))
    heapq.heappush(jewel, (M, V))

bag = []
for _ in range(K):
    C = int(sys.stdin.readline().rstrip())
    heapq.heappush(bag, C)

save_price = []
answer = 0
for a in range(K):
    size_of_bag = heapq.heappop(bag)
    while jewel:
        if size_of_bag >= jewel[0][0]:
            heapq.heappush(save_price, -jewel[0][1])
            heapq.heappop(jewel)
        else:
            break
    if save_price:
        answer -= heapq.heappop(save_price)

print(answer)

# import sys
# import heapq
#
# N, K = map(int, sys.stdin.readline().split(" "))
# jewel = []
# for _ in range(N):
#     M, V= map(int, sys.stdin.readline().split(" "))
#     heapq.heappush(jewel, (-M, -V))
#
# bag = []
# for _ in range(K):
#     C = int(sys.stdin.readline().rstrip())
#     heapq.heappush(bag, -C)
#
# answer = 0
# save_price = []
# for i in range(K):
#     size_of_bag = -(heapq.heappop(bag))
#     while jewel:
#         if -(jewel[0][0]) < size_of_bag:
#             heapq.heappush(save_price, jewel[0][1])
#             heapq.heappop(jewel)
#         else:
#             heapq.heappop(jewel)
#     if save_price:
#         answer -= heapq.heappop(save_price)
#
# print(answer)