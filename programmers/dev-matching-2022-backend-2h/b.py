def solution(leave, day, holidays):
    day_to_num = {
        "MON": 0,
        "TUE": 1,
        "WED": 2,
        "THU": 3,
        "FRI": 4,
        "SAT": 5,
        "SUN": 6,
    }
    day = day_to_num[day]

    parities = []
    for i in range(1, 31):
        if day == 5 or day == 6 or i in holidays:
            parities.append(1)
        else:
            parities.append(0)
        day = (day + 1) % 7

    answer = -1

    for i in range(len(parities)):
        leave_cnt = 0
        for tmp_answer, parity in enumerate(parities[i:], 1):
            if parity == 0:
                leave_cnt += 1
                if leave_cnt > leave:
                    break

            answer = max(tmp_answer, answer)

    return answer


leave = 4
day = "FRI"
holidays = [6, 21, 23, 27, 28]

answer = solution(leave, day, holidays)
print(answer)
