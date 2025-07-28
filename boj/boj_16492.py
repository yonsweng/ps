from sys import stdin


def has_single_character(s):
    return len(set(s)) == 1


def count_from_left(s, c):
    count = 0
    for char in s:
        if char == c:
            count += 1
        else:
            break
    return count


def solve():
    target = None
    gens = []
    dels = []
    while True:
        line = stdin.readline().strip()
        if line.startswith("target:"):
            target = line.split(":")[1].strip()
            break
        elif line.startswith("gen:"):
            start, end = line.split(":")[1].strip().split("->")
            gens.append((start.strip(), end.strip()))
        elif line.startswith("del:"):
            dels.append(line.split(":")[1].strip())

    current = "A"

    if current == target:
        print("O")
        return

    count = 10
    while count > 0:
        # Replace all occurrences of the start with the end
        i = 0
        while i < len(current):
            for gen in gens:
                if current[i:i + len(gen[0])] == gen[0]:
                    current = current[:i] + gen[1] + current[i + len(gen[0]):]
                    i += len(gen[1]) - 1  # Move past the newly inserted string
                    break
            i += 1

        i = 0
        while i < len(current):
            for del_item in dels:
                if has_single_character(del_item):
                    # Remove all occurrences of the single character which has the length over del_item
                    # For example, current = "AAAA", del_item = "AAA" -> current = ""
                    # current = "AA", del_item = "AAA" -> current = "AA"
                    if current[i:i + len(del_item)] == del_item:
                        c = count_from_left(current[i:], del_item[0])
                        current = current[:i] + current[i + c:]
                        i -= 1
                        break
                else:
                    # Remove all occurrences of the del_item
                    if current[i:i + len(del_item)] == del_item:
                        current = current[:i] + current[i + len(del_item):]
                        i -= 1
                        break
            i += 1

        if current == target:
            print("O")
            return
                
        count -= 1

    print("X")


if __name__ == "__main__":
    solve()
