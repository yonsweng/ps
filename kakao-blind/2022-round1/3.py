import math

def diff(t1, t2):
    h1, m1 = t1.split(':')
    h2, m2 = t2.split(':')
    h1, m1, h2, m2 = map(int, [h1, m1, h2, m2])
    return (h1 - h2) * 60 + m1 - m2


def solution(fees, records):
    park = {}
    answer = {}

    for record in records:
        time, num, inout = record.split()

        if inout == 'IN':
            park[num] = time
        else:
            if num in answer:
                answer[num] += diff(time, park[num])
            else:
                answer[num] = diff(time, park[num])
            park.pop(num)

    for num in park:
        if num in answer:
            answer[num] += diff('23:59', park[num])
        else:
            answer[num] = diff('23:59', park[num])

    for num in answer:
        answer[num] = fees[1] + max(0, math.ceil((answer[num] - fees[0]) / fees[2]) * fees[3])

    answer = sorted(list(answer.items()), key=lambda x: int(x[0]))
    answer = [fee for _, fee in answer]
    return answer


# fees = [180, 5000, 10, 600]
# records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
# result = [14600, 34400, 5000]

fees = [120, 0, 60, 591]
records = ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]
# result = [0, 591]

fees = [1, 461, 1, 10]
records = ["00:00 1234 IN"]
# result = [14600, 34400, 5000]

result = solution(fees, records)
print(result)
