def solution(enroll, referral, seller, amount):
    relationship = {}
    answer = {}

    for i in range(len(enroll)):
        answer[enroll[i]] = 0
        if referral[i] == "-":
            relationship[enroll[i]] = "center"
        else:
            relationship[enroll[i]] = referral[i]
    print(relationship)
    for j in range(1):
        name_of_seller = seller[j]
        # num_of_product
        num_of_product = amount[j] * 100
        while True:
            next_name = relationship[name_of_seller]
            if next_name == "center":
                break
            else:
                benefit = num_of_product * 0.1
                answer[name_of_seller] += num_of_product - benefit
                answer[next_name] += benefit
                print("배분", answer)
                name_of_seller = next_name
                num_of_product = benefit


    print(answer)

    return answer

print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
               ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
               ["young", "john", "tod", "emily", "mary"],
               [12, 4, 2, 5, 10]))