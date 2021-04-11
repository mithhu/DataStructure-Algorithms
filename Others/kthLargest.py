import heapq


def kthLargest(iterable, k):
    largest = []
    sortedArray = []
    for value in iterable:
        heapq.heappush(largest, value)
        if len(largest) > k:
            sortedArray.append(heapq.heappop(largest))
    if (len(largest) < k):
        return None
    return largest


print(kthLargest([8, 16, 80, 55, 32, 8, 38], 3))
