import heapq


def kthSmallest(iterable, k):
    smallest = []
    for value in iterable:
        print(smallest)
        heapq.heappush(smallest, -value)
        if len(smallest) > k:
            heapq.heappop(smallest)
    if (len(smallest) < k):
        return None
    return -smallest[0]


print(kthSmallest([8, 16, 80, 55, 32, 8, 38], 3))
