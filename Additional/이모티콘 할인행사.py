import heapq
from itertools import product

def solution(users, emoticons):
    discount_rate = [10,20,30,40]
    candidate = list(product(discount_rate, repeat=len(emoticons)))

    new_emoticons_price = []
    for candi in candidate:
        temp = []
        for rate, price in zip(candi, emoticons):
            temp.append(price * (100-rate) * 0.01)
        new_emoticons_price.append(temp)

    answer = []
    for i in range(len(new_emoticons_price)):
        all_user_total = 0
        plus = 0
        for j in range(len(users)):
            percent = users[j][0]
            max_price = users[j][1]
            user_total = 0
            flag = False
            for k in range(len(new_emoticons_price[i])):
                if not flag and candidate[i][k] >= percent:
                        user_total += new_emoticons_price[i][k]
                        if user_total >= max_price:
                            plus += 1
                            user_total = 0
                            flag = True
                        else:
                            pass
            if not flag:
                all_user_total += user_total
        heapq.heappush(answer, (-plus, -all_user_total))

    return [-answer[0][0], int(-answer[0][1])]


# 틀린 코드
# import heapq
# from itertools import product
#
# def solution(users, emoticons):
#     discount_rate = [10,20,30,40]
#     sorted_user = sorted(users, key=lambda x:x[0])
#     min_discount = sorted_user[0][0]
#
#     start = 0
#     for i in range(4):
#         if min_discount > discount_rate[i]:
#             start = i
#
#     candidate = list(product(discount_rate[start:], repeat=len(emoticons)))
#
#     new_emoticons_price = []
#
#     for candi in candidate:
#         temp = []
#         for rate, price in zip(candi, emoticons):
#             temp.append(price * (100-rate) * 0.01)
#
#         new_emoticons_price.append(temp)
#
#     answer = []
#     for i in range(len(new_emoticons_price)):
#         all_price = 0
#         plus = 0
#         for j in range(len(users)):
#             percent = users[j][0]
#             max_price = users[j][1]
#             total = 0
#             for k in range(len(new_emoticons_price[i])):
#                 if candidate[i][k] >= percent:
#                     total += new_emoticons_price[i][k]
#                     if total >= max_price:
#                         plus += 1
#                         total = 0
#                         continue
#             all_price += total
#         heapq.heappush(answer, (-plus, -all_price))
#
#     return [-answer[0][0], int(-answer[0][1])]


print(solution([[40, 10000], [25, 10000]], [7000, 9000]))
print(solution([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]], [1300, 1500, 1600, 4900]))
