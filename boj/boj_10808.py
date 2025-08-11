from sys import stdin


def solve():
    s = stdin.readline().strip()
    count = [0] * 26
    for char in s:
        count[ord(char) - ord('a')] += 1
    print(" ".join(map(str, count)))


if __name__ == "__main__":
    solve()
