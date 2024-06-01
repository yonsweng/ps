from sys import stdin

n = 0
numbers = []
operators = []
max_result = -1000000000
min_result = 1000000000


def dfs(idx, result):
    global max_result, min_result
    if idx == n:
        max_result = max(max_result, result)
        min_result = min(min_result, result)
        return
    for i in range(4):
        if operators[i] > 0:
            operators[i] -= 1
            if i == 0:
                dfs(idx + 1, result + numbers[idx])
            elif i == 1:
                dfs(idx + 1, result - numbers[idx])
            elif i == 2:
                dfs(idx + 1, result * numbers[idx])
            else:
                dfs(idx + 1, int(result / numbers[idx]))
            operators[i] += 1


def main():
    global n, numbers, operators
    n = int(stdin.readline())
    numbers = list(map(int, stdin.readline().split()))
    operators = list(map(int, stdin.readline().split()))
    dfs(1, numbers[0])
    print(max_result)
    print(min_result)


if __name__ == "__main__":
    main()
