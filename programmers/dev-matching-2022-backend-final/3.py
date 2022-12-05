def solution(subway, start, end):
    answer = 0

    n = len(subway)
    graph = [[9999] * n for _ in range(n)]
    for i in range(n):
        graph[i][i] = 0

    stations = []
    line_of_station = {}
    for line_num, line in enumerate(subway):
        s = set(map(int, line.split()))
        for i in s:
            line_of_station[i] = line_num
        stations.append(s)

    # print(stations)
    # print(line_of_station)

    for i in range(n):
        for j in range(i + 1, n):
            if len(stations[i].intersection(stations[j])) > 0:
                graph[i][j] = 1
                graph[j][i] = 1

    start = line_of_station[start]
    end = line_of_station[end]

    d = [9999] * n
    d[start] = 0
    started = set()
    for i in range(n):
        min_val = 9999
        mj = -1
        for j in range(n):
            if min_val > d[j] and j not in started:
                min_val = d[j]
                mj = j

        print(mj)

        if mj == -1:
            break

        for j in range(n):
            if d[mj] + graph[i][j] < d[j]:
                d[j] = d[mj] + graph[i][j]

        started.add(mj)

    answer = d[end]

    print(d)
    return answer


subway = ["1 2 3 4 5 6 7 8 9 10", "2 8"]
start = 1
end = 10
print(solution(subway, start, end))
