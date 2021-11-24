from sys import stdin


def read_input():
    n = int(stdin.readline().rstrip())
    a = list(map(int, stdin.readline().split()))
    return n, a


def is_kalindrome(n, a):
    left, right = 0, n - 1
    diff_left, diff_right = -1, -1
    while left < right:
        if a[left] != a[right]:
            diff_left = a[left]
            diff_right = a[right]
            break
        left += 1
        right -= 1

    if diff_left == -1:
        return True

    for diff in (diff_left, diff_right):
        left, right = 0, n - 1
        good = True
        while left < right:
            if a[left] != a[right]:
                if a[left] == diff:
                    left += 1
                elif a[right] == diff:
                    right -= 1
                else:
                    good = False
                    break
            else:
                left += 1
                right -= 1

        if good:
            return True

    return False


def solve(n, a):
    if is_kalindrome(n, a):
        return 'YES'
    else:
        return 'NO'


def main():
    t = int(stdin.readline())

    for _ in range(t):
        input = read_input()
        answer = solve(*input)
        print(answer)


if __name__ == '__main__':
    main()
