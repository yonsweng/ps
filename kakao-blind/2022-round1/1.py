def solution(id_list, report, k):
    answer = []

    reporting = {key: set() for key in id_list}
    reported = {key: set() for key in id_list}

    for r in report:
        reporter, reportee = r.split()
        reporting[reporter].add(reportee)
        reported[reportee].add(reporter)

    stopped = set()
    for reportee in reported:
        if len(reported[reportee]) >= k:
            stopped.add(reportee)

    for reporter in id_list:
        cnt = 0
        for reportee in reporting[reporter]:
            if reportee in stopped:
                cnt += 1
        answer.append(cnt)

    return answer


# id_list = ["muzi", "frodo", "apeach", "neo"]
# report = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
# k = 2
# result = [2, 1, 1, 0]

id_list = ["con", "ryan"]
report = ["ryan con", "ryan con", "ryan con", "ryan con"]
k = 3

answer = solution(id_list, report, k)
print(answer)
