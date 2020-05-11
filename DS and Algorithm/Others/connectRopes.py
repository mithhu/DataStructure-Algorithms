import heapq

# def __init__(self):
# self.cost = 0


def connectRopes(ropes):
    minH = []
    for value in ropes:
        heapq.heappush(minH, value)

    cost = 0
    while len(minH) >= 2:
        first = heapq.heappop(minH)
        second = heapq.heappop(minH)
        cost = cost + first + second
        heapq.heappush(minH, first+second)
    return cost


print(connectRopes([1, 18]))
print(connectRopes([1, 2, 5, 10, 35, 89]))
