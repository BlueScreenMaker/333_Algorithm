def solution(want, number, discount):
    answer = 0
    total = sum(number)
    length = len(discount)
    shopping = dict()
    for pair in zip(want, number):
        shopping[pair[0]] = pair[1]

    for i in range(length-total+1):
        buy = dict()
        for j in range(i,i+total):
            if discount[j] in buy.keys():
                buy[discount[j]] += 1
            else:
                buy[discount[j]] = 1

        if buy == shopping:
            answer += 1
    return answer

print(solution(["apple"],[10],["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"]))