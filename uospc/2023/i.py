from sys import stdin


def main():
    n = list(map(int, stdin.readline().rstrip()))

    length = len(n)

    dp = [0] * length + [-1]
    min_j = [[length] * 10 for _ in range(length)]

    for i in range(length - 2, -1, -1):
        min_j[i][:] = min_j[i + 1][:]
        min_j[i][n[i + 1]] = i + 1

        dp[i] = min(dp[min_j[i][k]] for k in range(10)) + 1

    answers = []

    for first in range(1, 10):
        i = 0
        while i < length and n[i] != first:
            i += 1
        if i == length:
            answers.append(str(first))
            break

        answer = [first]

        while i < length:
            min_dp = min(dp[min_j[i][k]] for k in range(10))
            next_i = length
            for k in range(10):
                if dp[min_j[i][k]] == min_dp:
                    next_i = min_j[i][k]
                    answer.append(k)
                    break
            i = next_i

        answer = "".join(map(str, answer))
        answers.append(answer)

    print(min(answers, key=lambda x: (len(x), x)))


if __name__ == "__main__":
    main()
