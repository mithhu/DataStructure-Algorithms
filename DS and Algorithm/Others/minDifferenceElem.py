def search(nums, target):
    start = 0
    end = len(nums) - 1
    while start <= end:
        mid = (start + end) // 2
        if nums[mid] == target:
            return nums[mid]
        if nums[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    if abs(nums[start] - target) < abs(nums[end] - target):
        return nums[start]
    else:
        return nums[end]


print(search([10, 15, 20, 35, 60, 70, 100], 45))
