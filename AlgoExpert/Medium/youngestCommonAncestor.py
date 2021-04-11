def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    depthOne = getDescendantDepth(topAncestor, descendantOne)
    depthTwo = getDescendantDepth(topAncestor, descendantTwo)
    if depthOne > depthTwo:
        return backtrackAncestralTree(descendantOne, descendantTwo, depthOne - depthTwo)
    else:
        return backtrackAncestralTree(descendantTwo, descendantOne, depthTwo - depthOne)


def getDescendantDepth(topAncestor, descendent):
    depth = 0
    while descendent != topAncestor:
        depth += 1
        descendent = descendent.ancestor
    return depth


def backtrackAncestralTree(lowerDescendent, higherDescendant, diff):
    while diff > 0:
        lowerDescendent = lowerDescendent.ancestor
        diff -= 1

    while lowerDescendent != higherDescendant:
        lowerDescendent = lowerDescendent.ancestor
        higherDescendant = higherDescendant.ancestor
    return lowerDescendent
