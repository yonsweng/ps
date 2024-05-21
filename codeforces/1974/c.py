from sys import stdin


def main():
    t = int(stdin.readline())
    for _ in range(t):
        n = int(stdin.readline())
        a = list(map(int, stdin.readline().split()))

        triples = [(a[i], a[i+1], a[i+2]) for i in range(0, n-2)]

        answer = 0

        groups = {}
        for a1, a2, a3 in triples:
            if (a1, a2) not in groups:
                groups[(a1, a2)] = {}
            if a3 not in groups[(a1, a2)]:
                groups[(a1, a2)][a3] = 0
            groups[(a1, a2)][a3] += 1
        for (a1, a2), group in groups.items():
            s = sum(group.values())
            s = s * (s - 1) // 2
            for a3, count in group.items():
                s -= count * (count - 1) // 2
            answer += s

        groups = {}
        for a1, a2, a3 in triples:
            if (a1, a3) not in groups:
                groups[(a1, a3)] = {}
            if a2 not in groups[(a1, a3)]:
                groups[(a1, a3)][a2] = 0
            groups[(a1, a3)][a2] += 1
        for (a1, a3), group in groups.items():
            s = sum(group.values())
            s = s * (s - 1) // 2
            for a2, count in group.items():
                s -= count * (count - 1) // 2
            answer += s

        groups = {}
        for a1, a2, a3 in triples:
            if (a2, a3) not in groups:
                groups[(a2, a3)] = {}
            if a1 not in groups[(a2, a3)]:
                groups[(a2, a3)][a1] = 0
            groups[(a2, a3)][a1] += 1
        for (a2, a3), group in groups.items():
            s = sum(group.values())
            s = s * (s - 1) // 2
            for a1, count in group.items():
                s -= count * (count - 1) // 2
            answer += s

        print(answer, flush=False)


if __name__ == "__main__":
    main()
