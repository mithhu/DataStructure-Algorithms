// function getNthFib(n) {
//   if (n === 2) {
//     return 1;
//   } else if (n == 1) {
//     return 0;
//   } else {
//     return getNthFib(n - 1) + getNthFib(n - 2);
//   }
// }

// function getNthFib(n, memoize = { 1: 0, 2: 1 }) {
//   if (n in memoize) {
//     return memoize[n];
//   }
//   return (memoize[n] = getNthFib(n - 1, memoize) + getNthFib(n - 2, memoize));
// }

function getNthFib(n) {
  const lastTwo = [0, 1];
  let counter = 3;
  while (counter <= n) {
    const newFib = lastTwo[0] + lastTwo[1];
    lastTwo[0] = lastTwo[1];
    lastTwo[1] = newFib;
    counter++;
  }

  return n > 1 ? lastTwo[1] : lastTwo[0];
}
console.log(getNthFib(8));
