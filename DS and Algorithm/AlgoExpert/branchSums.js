function branchSums(roor) {
    let sum = [];
    calculateBranchSums(root, 0, sum);
    return sum;
}

function calculateBranchSums(node, runningSum, sums) {
    if (node === null) {
        return
    }
    newRunningSum = runningSum + node.value;
    if (node.left === null && node.right === null) {
        sums.push(newRunningSum)
    }
    calculateBranchSums(node.left, newRunningSum, sums);
    calculateBranchSums(node.right, newRunningSum, sums)
}