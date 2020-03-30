function productSum(array, multiplier = 1) {
  let sum = 0;
  for (let element of array) {
    if (Array.isArray(element)) {
      sum += productSum(element, multiplier + 1);
    } else {
      sum += element;
    }
  }
  return sum * multiplier;
}

// let array = [5, 2, [7, -1], 3, [6, [-13, 8], 4]];
// console.log(productSum(array));
