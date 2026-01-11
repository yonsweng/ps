from sys import stdin


def solve():
    N = int(stdin.readline().strip())
    heights = list(map(int, stdin.readline().strip().split()))

    total_length = 0
    stack = []
    for height in heights:
        width = 0
        while stack and stack[-1][0] < height:
            width += stack[-1][1]
            stack.pop()

        if len(stack) == 0:
            stack.append((height, 1))
        else:
            if stack[-1][0] == height:
                total_length += width
                stack[-1] = (height, stack[-1][1] + width + 1)
            else:
                stack.append((height, width + 1))
    print(total_length)


if __name__ == "__main__":
    solve()
