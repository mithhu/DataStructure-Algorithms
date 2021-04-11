def search(nums, target):
    start = 0
    end = 1
    while target > nums[end]:
        start = end
        end = end * 2
    first = -1

    while start <= end:
        mid = (start + end) // 2
        if nums[mid] == target:
            first = mid
            end = mid - 1
        elif nums[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return first


print(search([0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1], 1))
