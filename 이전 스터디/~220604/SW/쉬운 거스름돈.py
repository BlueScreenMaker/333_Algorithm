N=int(input())
exchange_list=[] # 입력받은 거스름돈 저장하는 리스트
for i in range(0,N):
    exchange_list.append(int(input()))

for index, value in enumerate(exchange_list):
    temp= str(value)[:-1] #제일 뒤에 0은 무조건 붙는거고 계산할 때 필요없기 때문에 버리기
    spilt_list=(list(map(int, temp[::-1]))) # 숫자 뒤집기 EX) 16 → 61
    coin_list = [0, 0, 0, 0, 0, 0, 0, 0]
    flag=7 # 10원이 가장 끝에 있으므로 10원부터 비교할거니까 flag를 7로 둠
    N=0
    for worth in spilt_list:
        if(flag<=0):
            temp=worth*2 * (10**N)
            N += 1
            coin_list[0]+=temp
        elif (worth < 5):
            coin_list[flag] += worth
        else:
            num = worth - 5
            coin_list[flag] += num
            coin_list[flag-1]+=1
        flag-=2

    print('#%d'%(index+1))
    print(" ".join(map(str, coin_list)))
    spilt_list=[]


