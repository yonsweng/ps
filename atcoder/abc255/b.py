from sys import stdin
import math


def dist2(a, b):
    return (a[0] - b[0]) * (a[0] - b[0]) + (a[1] - b[1]) * (a[1] - b[1])


def main():
    n, k = map(int, stdin.readline().rstrip().split())
    a = list(map(int, stdin.readline().rstrip().split()))
    people = []
    for _ in range(n):
        x, y = map(int, stdin.readline().rstrip().split())
        people.append((x, y))

    print(
        math.sqrt(
            max(
                min(
                    dist2(person, people[ai-1])
                    for ai in a
                )
                for person in people
            )
        )
    )


if __name__ == '__main__':
    main()
