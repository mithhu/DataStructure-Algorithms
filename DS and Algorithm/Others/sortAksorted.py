import heapq


def sortAkSorted(iterable, k):
    largest = []
    sortedArray = []
    for value in iterable:
        heapq.heappush(largest, value)
        if len(largest) > k:
            sortedArray.append(heapq.heappop(largest))
    if (len(largest) < k):
        return None
    for elm in largest:
        sortedArray.append(elm)
    return sortedArray


print(sortAkSorted([8, 5, 3, 2, 8, 10, 9], 3))
