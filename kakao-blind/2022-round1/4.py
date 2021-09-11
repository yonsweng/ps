best_diff = 0
best_answer = [-1]


def dfs(i, n, point, info, answer):
    if i == 10:
        global best_diff, best_answer
        answer[-1] = n

        diff = 0
        for j in range(10):
            if info[j] >= answer[j]:
                if info[j] > 0:
                    diff -= 10 - j
            else:
                diff += 10 - j

        if best_diff < diff:
            best_diff = diff
            best_answer = answer[:]
        return

    if n <= info[i]:
        answer[i] = 0
        dfs(i+1, n, point, info, answer)
        return

    answer[i] = 0
    dfs(i+1, n, point, info, answer)

    answer[i] = info[i] + 1
    dfs(i+1, n-answer[i], point+(10-i), info, answer)


def solution(n, info):
    answer = [0] * 11

    dfs(0, n, 0, info, answer)

    return best_answer


n = 2
info = [1,0,0,0,0,0,0,0,0,0,1]

result = solution(n, info)
print(result)
