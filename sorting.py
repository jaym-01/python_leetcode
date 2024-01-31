from heapq import heapify, heappop


def merge_sort(a):
    if len(a) <= 1:
        return a

    mid = len(a) // 2

    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])

    out = []

    while len(left) > 0 or len(right) > 0:
        if len(left) == 0:
            out.append(right.pop(0))
        elif len(right) == 0:
            out.append(left.pop(0))
        else:
            out.append(left.pop(0) if left[0] < right[0] else right.pop(0))

    return out

def quicksort(a):
    if len(a) <= 1:
        return a

    mid = len(a) // 2

    pivot = a.pop(mid)

    l, r = 0, len(a) - 1

    while l <= r:
        if a[l] > pivot and a[r] < pivot:
            tmp = a[l]
            a[l] = a[r]
            a[r] = tmp

        if a[l] < pivot:
            l += 1
        
        if a[r] > pivot:
            r -= 1

    # print("l: ", l, "\nr: ", r)
    return quicksort(a[:l]) + [pivot] + quicksort(a[l:])

def heapSort(a):
    heapify(a)
    stack = []
    out = []

    while len(a) > 0:
        stack.append(heappop(a))
    
    return stack

if __name__ == "__main__":
    tmp = [9, 12, 26, 25, 22, 15, 4, 24, 20, 27, 14, 10, 19, 21, 8, 23, 13, 29, 18, 7, 1, 11, 5, 17, 2, 28, 30, 3, 6, 16]

    print(heapSort(tmp))