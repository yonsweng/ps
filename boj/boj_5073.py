from sys import stdin


def solve():
    while True:
        a, b, c = map(int, stdin.readline().strip().split())
        if a == 0 and b == 0 and c == 0:
            break
        sides = sorted([a, b, c])
        if sides[0] + sides[1] <= sides[2]:
            print("Invalid")
        elif sides[0] == sides[1] == sides[2]:
            print("Equilateral")
        elif sides[0] == sides[1] or sides[1] == sides[2]:
            print("Isosceles")
        else:
            print("Scalene")


if __name__ == "__main__":
    solve()
