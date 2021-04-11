function binarySearch(array, target) {
  return binarySearchHelper(array, target, 0, array.length - 1);
}

function binarySearchHelper(array, target, left, right) {
  while (left <= right) {
    const middle = Math.floor((left + right) / 2);
    const potentialMatch = array[middle];
    if (target === potentialMatch) {
      return middle;
    } else if (target < potentialMatch) {
      right = middle - 1;
    } else {
      left = middle + 1;
    }
  }
  return -1;
}

//recursive
// function binarySearchHelper(array, target, left, right) {
//   if (left > right) return -1;
//   const middle = Math.floor((left + right) / 2);
//   const potentialMatch = array[middle];
//   if (target === potentialMatch) {
//     return middle;
//   } else if (target < potentialMatch) {
//     return binarySearchHelper(array, target, left, middle - 1);
//   } else {
//     return binarySearchHelper(array, target, middle + 1, right);
//   }
// }

console.log(binarySearch([1, 2, 3, 4, 5, 6], 5));
