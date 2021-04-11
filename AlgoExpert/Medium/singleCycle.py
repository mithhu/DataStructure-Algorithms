def has_single_cycle(array):
    numOfElelmentVisited = 0
    currentIndex = 0

    while numOfElelmentVisited < len(array):
        if currentIndex == 0 and numOfElelmentVisited > 0:
            return False
        numOfElelmentVisited += 1
        currentIndex = getNextIndex(currentIndex, array)
    return currentIndex == 0


def getNextIndex(currentIndex, array):
    jump = array[currentIndex]
    nextIdx = (currentIndex + jump) % len(array)
    return nextIdx if nextIdx >= 0 else nextIdx + len(array)


input_array = [2, 3, 1, -4, -4, 2]
print("Is Single Cycle: ", has_single_cycle(input_array))
