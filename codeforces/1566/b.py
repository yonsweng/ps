def main():
    t = int(input())
    for _ in range(t):
        s = input().split('1')
        answer = 0
        for p in s:
            if p != '':
                answer += 1
        answer = min(answer, 2)
        print(answer)


if __name__ == '__main__':
    main()
