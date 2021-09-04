def find_pivot_idx(arr):
    i = 0
    for j in range(len(arr) - 1):
        if arr[j] <= arr[-1]:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[-1] = arr[-1], arr[i]
    return i


def quick_select(arr, k):
    '''
    Find k-th element in arr.
    '''
    pivot_idx = find_pivot_idx(arr)
    if k - 1 == pivot_idx:
        return arr[pivot_idx]
    elif k - 1 < pivot_idx:
        return quick_select(arr[:pivot_idx], k)
    else:
        return quick_select(arr[pivot_idx+1:], k - (pivot_idx+1))


arr = list(map(int, input().split()))
k = int(input())

answer = quick_select(arr, k)
print(answer)
