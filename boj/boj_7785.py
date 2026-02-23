from sys import stdin


def solve():
    n = int(stdin.readline())
    people = {}
    for _ in range(n):
        name, behavior = stdin.readline().split()
        if behavior == "enter":
            people[name] = people.get(name, 0) + 1
        else:
            people[name] = people.get(name, 0) - 1
            if people[name] == 0:
                del people[name]

    for name in sorted(people.keys(), reverse=True):
        for _ in range(people[name]):
            print(name, flush=False)


if __name__ == "__main__":
    solve()
