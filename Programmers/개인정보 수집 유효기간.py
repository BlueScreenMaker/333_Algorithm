def solution(today, terms, privacies):
    answer = []
    validate_period = {}
    for a in range(len(terms)):
        check, period = terms[a].split(" ")
        validate_period[check] = int(period)
    today_year, today_month, today_day = map(int, today.split("."))
    for i in range(len(privacies)):
        day, option = privacies[i].split(" ")
        year, month, day = map(int, day.split("."))
        cal_month = month + validate_period[option]

        cal_day, cal_year = day, year
        # day가 1일일 경우
        if day == 1:
            cal_month -= 1
            cal_day = 28
        else:
            cal_day -= 1

        # 계산한 날짜가 12월을 넘어서는 경우
        if cal_month > 12:
            year_gap = cal_month // 12
            cal_month = cal_month % 12
            # 12로 딱 나눠떨어지는 경우,
            # 12월달로 설정하고 년도를 하나 빼줘야함
            if cal_month == 0:
                cal_month = 12
                year_gap -= 1
            cal_year += year_gap
        print(cal_year, cal_month, cal_day)
        if today_year > cal_year:
            answer.append(i+1)
        elif today_year == cal_year:
            if today_month > cal_month:
                answer.append(i+1)
            elif today_month == cal_month:
                if today_day > cal_day:
                    answer.append(i+1)

    answer.sort()
    return answer

print(solution( "2009.12.28", ["A 13"], ["2008.11.03 A"]))

# print(solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))