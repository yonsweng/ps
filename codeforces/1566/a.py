def main():
    t = int(input())
    for _ in range(t):
        n, s = map(int, input().split())
        answer = s // (n // 2 + 1)
        print(answer)


if __name__ == '__main__':
    main()
