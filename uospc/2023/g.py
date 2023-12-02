from sys import stdin


def main():
    n, k = map(int, stdin.readline().split())
    m = []
    for _ in range(n):
        m.append(list(map(int, stdin.readline().split())))

    m.sort(key=lambda x: x[1])

    ans = 0
    rooms = [0] * k
    for s, e in m:
        # get the index having the maximum value in rooms
        i = max(range(k), key=lambda x: rooms[x] if rooms[x] < s else -1)
        if rooms[i] < s:
            rooms[i] = e
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
