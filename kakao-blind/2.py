def all_substr(s):
    lst = []
    for i in range(1, 2 ** len(s)):
        tmp = []
        for j in range(len(s)):
            if (1 << j) & i:
                # print(j)
                tmp.append(s[j])
        lst.append(''.join(tmp[::-1]))
    return lst

def solution(orders, course):
    answer = []
    cnt = {}
    for order in orders:
        for substr in all_substr(order):
            substr.sort()
            if substr not in cnt:
                cnt[substr] = 0
            cnt[substr] += 1
            
    sorted_cnt = sorted(cnt.items(), key=lambda x: len(x[0]), reverse=True)
    
#     for s, c in sorted_cnt:
#         if c >= 2:
#             answer.append(s.sort())
#             for z in all_substr(s):
                
            
    print(sorted_cnt)
    return answer