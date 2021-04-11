import heapq


def topKFrequent(nums, k):
    obj = {}
    for i in nums:
        if i in obj:
            obj[i] += 1
        else:
            obj[i] = 1
    maxH = []
    for key in obj:
        heapq.heappush(maxH, (obj[key], key))
        if len(maxH) > k:
            heapq.heappop(maxH)
    res = []

    while len(maxH) > 0:
        res.append(maxH[0][1])
        heapq.heappop(maxH)
    return res


print(topKFrequent([1, 1, 1, 2, 2, 3], 2))
