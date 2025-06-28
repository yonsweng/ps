from sys import stdin


def solve():
    n = int(stdin.readline().strip())
    for _ in range(n):
        line = list(map(int, stdin.readline().strip().split()))
        k = line[0]
        s = line[1:]

        a = s[0]
        u, v = 0, 1
        found = False
        for _ in range(9):
            if (s[1] - u * a) % v == 0:
                x = (s[1] - u * a) // v
                uu, vv = u, v
                i = 2
                cnt = 1
                while i < k:
                    uu, vv = vv, uu + vv
                    if uu * a + vv * x == s[i]:
                        i += 1
                        cnt = 1
                    else:
                        cnt += 1
                        if cnt == 10:
                            break
                if cnt != 10:
                    answer = [a]
                    uu, vv = 0, 1
                    for _ in range(4):
                        answer.append(uu * a + vv * x)
                        uu, vv = vv, uu + vv
                    print("STABLE", " ".join(map(str, answer)), flush=False)
                    found = True
                    break
            u, v = v, u + v
        if not found:
            print("UNSTABLE", flush=False)


if __name__ == "__main__":
    solve()
