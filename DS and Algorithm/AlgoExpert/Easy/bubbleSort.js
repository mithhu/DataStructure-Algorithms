function bubbleSort(array) {
  let isSorted = false;
  let counter = 0;
  while (!isSorted) {
    isSorted = true;
    for (let i = 0; i < array.length - 1 - counter; i++) {
      if (array[i] > array[i + 1]) {
        swap(i, i + 1, array);
        isSorted = false;
      }
    }
    counter++;
  }
  return array;
}

function swap(i, j, array) {
  let temp = array[j];
  array[j] = array[i];
  array[i] = temp;
}

console.log(bubbleSort([8, 5, 2, 9, 5, 6, 3]));
