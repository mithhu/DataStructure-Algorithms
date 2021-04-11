def mergeSort(array):
    if len(array) == 1:
        return array

    middleIdx = len(array) // 2
    leftHalf = array[:middleIdx]
    rightHalf = array[middleIdx:]
    return mergeSortedArrays(mergeSort(leftHalf), mergeSort(rightHalf))


def mergeSortedArrays(leftHalf, rightHalf):
    sortedArrays = [None] * (len(leftHalf) + len(rightHalf))
    k = i = j = 0
    while i < len(leftHalf) and j < len(rightHalf):
        if leftHalf[i] <= rightHalf[j]:
            sortedArrays[k] = leftHalf[i]
            i += 1
        else:
            sortedArrays[k] = rightHalf[j]
            j += 1
        k += 1

    while i < len(leftHalf):
        sortedArrays[k] = leftHalf[i]
        i += 1
        k += 1
    while j < len(rightHalf):
        sortedArrays[k] = rightHalf[j]
        j += 1
        k += 1
    return sortedArrays


# def mergeSort(array):
#     if len(array) <= 1:
#         return array
#     auxilaryArray = array[:]
#     mergeSortHelper(array, 0, len(array)-1, auxilaryArray)
#     return array

# def mergeSortHelper(mainArray, startIdx, endIdx, auxilaryArray):
#     if startIdx == endIdx:
#         return
#     middleIdx = (startIdx + endIdx) // 2
#     mergeSortHelper(auxilaryArray, startIdx, middleIdx, mainArray)
#     mergeSortHelper(auxilaryArray, middleIdx+1, endIdx, mainArray)
#     doMerge(mainArray, startIdx, middleIdx, endIdx, auxilaryArray)


# def doMerge(mainArray, startIdx, middleIdx, endIdx, auxilaryArray):
#     k = startIdx
#     i = startIdx
#     j = middleIdx + 1
#     while i <= middleIdx and j <= endIdx:
#         if auxilaryArray[i] <= auxilaryArray[j]:
#             mainArray[k] = auxilaryArray[i]
#             i += 1
#         else:
#             mainArray[k] = auxilaryArray[j]
#             j += 1
#         k += 1

#     while i <= middleIdx:
#         mainArray[k] = auxilaryArray[i]
#         i += 1
#         k += 1
#     while j <= endIdx:
#         mainArray[k] = auxilaryArray[j]
#         j += 1
#         k += 1

print(mergeSort([2, 3, 1]))
