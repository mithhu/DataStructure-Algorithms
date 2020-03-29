// function caesarCipher(string, key) {
//   const newLetters = [];
//   const newKey = key % 26;
//   const alphabet = "abcdefghijklmnopqrstuvwxyz".split("");
//   for (const letter of string) {
//     newLetters.push(getNewLetter(letter, newKey, alphabet));
//   }
//   return newLetters.join("");
// }

// function getNewLetter(letter, key, alphabet) {
//   const newLetterCode = alphabet.indexOf(letter) + key;
//   return newLetterCode <= 25
//     ? alphabet[newLetterCode]
//     : alphabet[-1 + (newLetterCode % 25)];
// }

// Time - O(n), Space - O(n)

function caesarCipher(string, key) {
  const newLetters = [];
  const newKey = key % 26;
  for (const letter of string) {
    newLetters.push(getNewLetter(letter, newKey));
  }
  return newLetters.join("");
}

function getNewLetter(letter, key) {
  const newLetterCode = letter.charCodeAt() + key;
  return newLetterCode <= 122
    ? String.fromCharCode(newLetterCode)
    : String.FromCharCode(96 + (newLetterCode % 122));
}

console.log(caesarCipher("abc", 2));
