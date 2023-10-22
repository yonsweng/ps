def suffix_array(s):
    """
    sa[i]: k such that s[k:] is the i-th smallest suffix of s
    g[i]: group number of s[i:]
    """
    sa = [i for i in range(len(s))]
    g = [ord(c) - ord("a") for c in s] + [-1]

    t = 1
    while t < len(s):
        sa.sort(key=lambda x: (g[x], g[min(x + t, len(s))]))
        g2 = [0] * len(s) + [-1]
        g2[sa[0]] = 0
        for i in range(1, len(s)):
            if g[sa[i]] == g[sa[i - 1]] and g[sa[i] + t] == g[sa[i - 1] + t]:
                g2[sa[i]] = g2[sa[i - 1]]
            else:
                g2[sa[i]] = g2[sa[i - 1]] + 1
        g = g2
        t *= 2

    return sa


def longest_common_prefix(s, sa):
    """
    lcp[i]: longest common prefix of s[sa[i]:] and s[sa[i+1]:]
    rank[i]: inverse of sa[i]
    """
    lcp = [0] * len(s)

    rank = [0] * len(s)
    for i in range(len(s)):
        rank[sa[i]] = i

    h = 0
    for i in range(len(s)):
        if rank[i] == 0:
            continue
        j = sa[rank[i] - 1]
        while i + h < len(s) and j + h < len(s) and s[i + h] == s[j + h]:
            h += 1
        lcp[rank[i]] = h
        if h > 0:
            h -= 1

    return lcp


def main():
    _ = int(input())
    s = input()

    sa = suffix_array(s)

    lcp = longest_common_prefix(s, sa)
    print(max(lcp))


if __name__ == "__main__":
    main()
