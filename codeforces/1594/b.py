from sys import stdin


def read_input():
    n, k = map(int, stdin.readline().split())
    return n, k


def convert_to_binary(k):
    '''
    Return ex) [0, 0, 1, 1] for 1100(2)
    '''
    binary = []
    while k > 0:
        binary.append(k % 2)
        k //= 2
    return binary


def calc_answer(n, binary):
    answer = 0
    for i, b in enumerate(binary):
        if b == 1:
            answer = (answer + pow(n, i, 1000000007)) % 1000000007
    return answer


def solve(n, k):
    binary = convert_to_binary(k)
    # print(binary)
    answer = calc_answer(n, binary)
    # answer = 0
    return answer


def main():
    t = int(stdin.readline())

    for _ in range(t):
        input = read_input()
        answer = solve(*input)
        print(answer)


if __name__ == '__main__':
    main()
