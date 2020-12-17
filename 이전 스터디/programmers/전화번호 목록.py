def solution(phone_book):
    answer = True
    number_list=list(map(str, phone_book))
    number_list.sort()
    for i in range(0,len(number_list)-1):
        for j in range(i+1, len(number_list)):
            if(number_list[j].startswith(number_list[i])):
                # 접두사가 같은지 확인
                answer=False
                break;
        if(answer==False):
            break;
    return answer


'''
def solution(phone_book):
    answer = True
    number_list=list(map(int, phone_book))
    number_list.sort()
    # 입력 받은 전화번호부를 int형울 바꿔서 정렬
    # 나는 아직도 정렬이 왜 빠른지 모르겠다
    for i in range(0,len(number_list)-1):
        for j in range(i+1, len(number_list)):
            temp=str(number_list[j])
            # 일단 임시 변수에 number_list[j]값을 저장
            if(str(number_list[i])==temp[0:len(str(number_list[i]))]):
                # 접두사가 같은지 확인
                answer=False
                break;
        if(answer==False):
            # 접두사 같은거 일단 발견되면 굳이 더 돌릴 필요없으니 검사하고 빠져나옴
            # 이거 하나 추가하니까 효율성 통과하더라 엥쯧엥쯧
            break;
    return answer
'''
'''
def solution(phone_book):
    answer = True
    for i in range(0,len(phone_book)):
        for j in range(i+1, len(phone_book)):
            if(len(phone_book[i])<=len(phone_book[j])):
                temp=phone_book[j]
                if(phone_book[i]==temp[0:len(phone_book[i])]):
                    answer=False
                    break;
    return answer
'''