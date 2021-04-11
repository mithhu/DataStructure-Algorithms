def search(nums, target):
    start = 0
    end = 1
    while target > nums[end]:
        start = end
        end = end * 2
    # can use binary search function too
    while start <= end:
        mid = (start + end) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return -1


print(search([10, 15, 20, 35, 60, 70, 100], 60))
