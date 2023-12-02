from sys import stdin
from math import log10


def main():
    k = int(stdin.readline())

    j = 0
    cnt = 9
    length = 1
    while k > j + cnt * length:
        j += cnt * length
        cnt *= 10 if length % 2 == 0 else 1
        length += 1

    order = (k - j + length - 1) // length
    r = (k - j + length - 1) % length
    first = (order - 1) // (cnt // 9) + 1
    others_len = int(log10(float(cnt // 9)))
    others = str(order - (first - 1) * (cnt // 9) - 1).zfill(others_len)
    ans = str(first) + others[:others_len]
    if length % 2 == 0:
        ans = ans + ans[::-1]
    else:
        ans = ans + ans[:-1][::-1]
    # print(ans)
    print(ans[r])


if __name__ == "__main__":
    main()
