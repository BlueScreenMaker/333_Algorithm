def solution(n, t, m, timetable):
    answer = '09:00'
    new_time=[]
    for time in timetable:
        hour=int(time[:2])
        minute=int(time[3:])
        new_time.append((hour*60)+minute)

    new_time.sort()

    bus_time=[540]
    for i in range(1,n):
        bus_time.append(540+(i*t))

    passenger=0
    for check in bus_time:
        count = 0
        while count < m and passenger < len(new_time) and new_time[passenger] <= check:
            count += 1
            passenger += 1
        if count < m :
            answer = check
        else:
            answer=new_time[passenger-1]-1

    # zfill => 00 숫자 맞추기
    answer = str(answer//60).zfill(2) + ":" + str(answer%60).zfill(2)

    return answer

print(solution(1,1,5,["08:00", "08:01", "08:02", "08:03"]))