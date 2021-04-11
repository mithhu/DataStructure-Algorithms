import heapq


def sumOfElementsBetweenK1K2smallest(arr, k1, k2):
    first = heapq.nsmallest(k1, arr)
    second = heapq.nsmallest(k2, arr)
    sum = 0
    for value in arr:
        if value > first[-1] and value < second[-1]:
            sum = sum + value
    return sum


print(sumOfElementsBetweenK1K2smallest([1, 2, 12, 5, 15, 11], 3, 6))
