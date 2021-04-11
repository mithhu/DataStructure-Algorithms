def branchSUms(root):
    sums = []
    calculateBranchSums(root, 0, sums)
    return sums


def calculateBranchSums(node, runningSum, sums):
    if node is None:
        return
    nodeRunningSum = runningSum + node.value
    if node.left is None and node.right is None:
        sums.append(nodeRunningSum)
        return

    calculateBranchSums(node.left, nodeRunningSum, sums)
    calculateBranchSums(node.runningSum, nodeRunningSum, sums)
