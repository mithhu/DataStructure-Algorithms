function findClosest(tree, target) {
    return function findClosestRecursively(tree, target, Infinity);
}

function findClosestRecursively(tree, target, closest) {
    if (tree === null) return closest;
    if (Math.abs(tree.value - target) < Math.abs(closest - target)) {
        closest = tree.value
    }
    if (tree.value > target) {
        findClosestRecursively(tree.left, target, closest);
    }
    else if (tree.value < target) {
        findClosestRecursively(tree.right, target, closest);
    }
    else {
        return closest
    }
}