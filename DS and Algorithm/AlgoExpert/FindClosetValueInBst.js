// Solution 1: 
function findClosest(tree, target) {
    return findClosestRecursively(tree, target, Infinity);
}

function findClosestRecursively(tree, target, closest) {
    if (tree === null) return closest;
    if (Math.abs(tree.value - target) < Math.abs(closest - target)) {
        closest = tree.value
    }
    if (tree.value > target) {
        findClosestRecursively(tree.left, target, closest);
    } else if (tree.value < target) {
        findClosestRecursively(tree.right, target, closest);
    } else {
        return closest
    }
}

//Soltion 2:
function findClosest(tree, target) {
    return findClosestIteratively(tree, target, Infinity);
}

function findClosestIteratively(tree, target, Infinity) {
    let currentNode = tree;
    let closest = Infinity;
    while (currentNode !== null) {
        if (Math.abs(currentNode.value - target) < Math.abs(closest - target)) {
            closest = currentNode.value
        }
        if (currentNode.value > target) {
            currentNode = currentNode.left
        } else if (currentNode.value < target) {
            currentNode = currentNode.right
        } else { break }
    }
    return closest
}
