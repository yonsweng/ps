A = int(input())

for x in range(1, A + 1):
    S = input()

    cnt = [0] * 26
    for s in S:
        cnt[ord(s) - ord('a')] += 1

    A = []
    possible = True

    for i, s in enumerate(S):
        max_cnt, max_ch_num = 0, 0
        for ch_num in range(26):
            if ch_num != ord(s) - ord('a') and cnt[ch_num] > max_cnt:
                max_cnt = cnt[ch_num]
                max_ch_num = ch_num

        if max_cnt == 0:
            A.append(ord(s))
            for j, a in enumerate(A):
                if ord(S[j]) != A[i] and ord(s) != a:
                    A[i], A[j] = A[j], A[i]
                    break
            if ord(s) == A[-1]:
                possible = False
                break
        else:
            cnt[max_ch_num] -= 1
            A.append(max_ch_num + ord('a'))

    print(f'Case #{x}: {"".join([chr(a) for a in A]) if possible else "IMPOSSIBLE"}')
