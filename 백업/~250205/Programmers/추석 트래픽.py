from collections import defaultdict
import copy
def solution(lines):
    answer = 0
    start_time = []
    end_time = []
    for line in lines:
        date, time, processing = line.split(" ")
        # 시간, 분, 초, 밀리 초로 쪼개기
        hour, min, second = time.split(":")
        s, ms = second.split(".")
        # 처리 후 시간
        a_time = int(hour) * (3_600_000) + int(min) * (60_000) + int(s) * (1_000) + int(ms)

        processing = processing[:-1]
        # 처리 전 시간 (더하기 1 > 시작 시간과 끝 시간을 포함함으로)
        b_time = int(a_time - (float(processing) * (1_000))) + 1

        start_time.append(b_time)
        end_time.append(a_time)

    for i in range(len(lines)):
        cnt = 0
        cur_end_time = end_time[i]
        for j in range(i, len(lines)):
            if cur_end_time > start_time[j] - 1000:
                cnt += 1
        answer = max(answer, cnt)


    return answer

print(solution(["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"]))