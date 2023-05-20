from sys import stdin


def main():
    n = int(stdin.readline())
    words = []
    for _ in range(n):
        words.append(stdin.readline().strip())

    # sort words by (length, dictionary order) and remove duplicates
    words = sorted(list(set(words)), key=lambda x: (len(x), x))

    # print words line by line
    for word in words:
        print(word, flush=False)


if __name__ == "__main__":
    main()
