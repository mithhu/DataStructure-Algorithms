def findCount(A, B):
    start = 0
    end = len(A) - 1
    res = -1
    while start <= end:
        mid = start + ((end-start) // 2)
        if A[mid] == B:
            res = mid
            # end = mid - 1
            start = mid + 1
        elif A[mid] > B:
            end = mid - 1
        else:
            start = mid + 1
    return res


print(findCount([5, 7, 7, 8, 8, 10], 8))
