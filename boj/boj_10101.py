from sys import stdin


def solve():
    a = int(stdin.readline())
    b = int(stdin.readline())
    c = int(stdin.readline())

    if a == b == c == 60:
        print('Equilateral')
    elif a + b + c == 180:
        if a == b or b == c or c == a:
            print('Isosceles')
        else:
            print('Scalene')
    else:
        print('Error')


if __name__ == "__main__":
    solve()
