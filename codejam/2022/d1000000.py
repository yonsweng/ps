from sys import stdin

T = int(stdin.readline())

for x in range(1, T+1):
    N = int(stdin.readline())
    S = list(map(int, stdin.readline().split()))

    S.sort()

    lower_bound, answer = 1, 0
    for Si in S:
        if Si >= lower_bound:
            answer += 1
            lower_bound += 1

    print(f'Case #{x}: {answer}')
