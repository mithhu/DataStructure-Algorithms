// Time - O(n^2), Space - O(n)
// function isPalindrome(string) {
//   let reversedString = "";
//   for (let i = string.length - 1; i >= 0; i--) {
//     reversedString += string[i];
//   }
//   return string === reversedString;
// }

// Time - O(n), Space - O(n)
// function isPalindrome(string) {
//   const reversedChars = [];
//   for (let i = string.length - 1; i >= 0; i--) {
//     reversedChars.push(string[i]);
//   }
//   return string === reversedChars.join("");
// }

//Recursion - Time - O(n), Space - O(n)
// function isPalindrome(string, i = 0) {
//   const j = string.length - 1 - i;
//   return i >= j ? true : string[i] === string[j] && isPalindrome(string, i + 1);
// }

//time - O(N), Space - O(1)
function isPalindrome(string) {
  let leftIdx = 0;
  let rightIdx = string.length - 1;
  while (leftIdx < rightIdx) {
    if (string[leftIdx] !== string[rightIdx]) return false;
    leftIdx++;
    rightIdx--;
  }

  return true;
}

console.log(isPalindrome("abcba"));
