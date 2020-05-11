import heapq


def kClosest(iterable, k, x):
    smallest = []
    closest = []
    for value in iterable:
        newValue = abs(value - x)
        heapq.heappush(smallest, (-newValue, -value))
        if len(smallest) > k:
            heapq.heappop(smallest)
    if (len(smallest) < k):
        return None
    print(smallest)
    while len(smallest) > 0:
        closest.append(-smallest[0][1])
        heapq.heappop(smallest)
    return sorted(closest)


print(kClosest([1, 2, 3, 4, 5], 4, 3))
