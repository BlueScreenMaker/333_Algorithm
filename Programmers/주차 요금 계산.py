import math

def solution(fees, records):
    answer = []

    info={}
    price={}

    for check in records:
        temp_list=list(check.split(" "))
        # 1번째 : 차랑넘버  0 : 시간
        if temp_list[2]=="IN":
            info[temp_list[1]]=temp_list[0]
        else:
            time = 0
            start_hour, start_min=map(int,info[temp_list[1]].split(":"))
            end_hour, end_min=map(int,temp_list[0].split(":"))
            # 들어온시간 : 6시 50
            # 나간시간 : 13시 20분
            # 나간 시간(분) - 들어온 시간의 (분) = 80(20+60) - 50 음수
            if end_min<start_min:
                end_min+=60
                end_hour-=1
                time+=end_min-start_min
                time+=(end_hour-start_hour)*60
            else:
                time+=end_min-start_min
                time+=(end_hour-start_hour)*60

            if temp_list[1] in price:
                price[temp_list[1]]+=time
            else:
                price[temp_list[1]]=time

            del info[temp_list[1]]

    for key,value in info.items(): # 23시 59분까지 출차가 되지 않는 경우
        redun_time=0
        point_hour, point_min=map(int,value.split(":"))
        redun_time+=59-point_min
        redun_time += (23 - point_hour)*60
        if key in price: # case 3번, 들어오기만하고 끝까지 안나가면 결국 price에 차 number가 없음
            price[key]+=redun_time
        else:
            price[key]=redun_time

    for key, value in price.items():
        base=value-fees[0]
        if base>0:
            extra=math.ceil(base/fees[2])
            price[key]=fees[1]+(extra*fees[3])
            # extra 식을 그대로 집어넣어도 상관 X
            # 식이 길어져서 보기 번거로워서 그냥 따로 뺌
        else:
            price[key]=fees[1]

    price=sorted(price.items())
    for x,y in price:
        answer.append(y)
    return answer

print(solution([180, 5000, 10, 600],
               ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT",
                "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
# print(solution([120, 0, 60, 591],["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]))
print(solution([1, 461, 1, 10],["00:00 1234 IN"]))