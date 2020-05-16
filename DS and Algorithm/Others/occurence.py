def findCount(nums, target):
    start = 0
    end = len(nums) - 1
    first = -1
    last = -1
    while start <= end:
        mid = start + ((end-start) // 2)
        if nums[mid] == target:
            first = mid
            end = mid - 1
        elif nums[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    start = 0
    end = len(nums) - 1
    while start <= end:
        mid = start + ((end-start) // 2)
        if nums[mid] == target:
            last = mid
            start = mid + 1
        elif nums[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    if first == -1:
        return 0
    return (last - first + 1)


print(findCount([3, 5, 5, 5, 5, 7, 8, 8], 3))
