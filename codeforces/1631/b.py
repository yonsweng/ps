from sys import stdin


def main():
    t = int(stdin.readline())
    for _ in range(t):
        n = int(stdin.readline())
        a = list(map(int, stdin.readline().split()))
        
        answer = 0
        i = n - 1
        while i >= 0:
            while i >= 0 and a[i] == a[-1]:
                i -= 1
            if i == -1:
                break
            answer += 1
            i = n - (n - i - 1) * 2 - 1

        print(answer)


if __name__ == '__main__':
    main()
