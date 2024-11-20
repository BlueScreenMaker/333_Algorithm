def check(bin_num, idx, deep):
    if deep == 0:
        return True

    elif bin_num[idx] == "0":
        if bin_num[idx - deep] == "1" or bin_num[idx + deep] == "1":
            return False

    left = check(bin_num, idx - deep, deep // 2)
    right = check(bin_num, idx + deep, deep // 2)
    return left and right

def solution(numbers):
    answer = []

    for num in numbers:
        bin_num = format(num, "b")
        nodes = format(len(bin_num) + 1, "b")

        if "1" in nodes[1:]:
            dummy = (1<<len(nodes)) - int(nodes, 2)
            bin_num = "0" * dummy + bin_num

        result = check(bin_num, len(bin_num)//2, (len(bin_num)+1)//4)

        if result:
            answer.append(1)
        else:
            answer.append(0)

    return answer


print(solution([7, 42, 5]))