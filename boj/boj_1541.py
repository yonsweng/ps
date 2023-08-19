from sys import stdin


def main():
    s = stdin.readline().rstrip()
    s = s.split("-")
    ans = 0
    for i in s[0].split("+"):
        ans += int(i)
    for i in s[1:]:
        for j in i.split("+"):
            ans -= int(j)
    print(ans)


if __name__ == "__main__":
    main()
