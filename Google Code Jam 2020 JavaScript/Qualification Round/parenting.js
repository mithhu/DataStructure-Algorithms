// const input = [
//   "4",
//   "3",
//   "360 480",
//   "420 540",
//   "600 660",
//   "3",
//   "0 1440",
//   "1 3",
//   "2 4",
//   "5",
//   "99 150",
//   "1 100",
//   "100 301",
//   "2 5",
//   "150 250",
//   "2",
//   "0 720",
//   "720 1440",
// ];

const fs = require("fs");
const input = fs.readFileSync(0, "utf8").trim().split("\n");

let currentline = 0;
function readline() {
  return input[currentline++];
}

let T = readline();

for (let i = 1; i <= T; i++) {
  let N = readline();
  let arr = [];
  for (let m = 0; m < N; m++) {
    arr.push(readline().split(" "));
  }
  console.log(`Case #${i}`, solve(arr));
}

function sortWithIndex(list) {
  let newArr = [];
  list.map((el, i) => {
    newArr.push([...el, i]);
  });

  newArr.sort((a, b) => a[0] - b[0]);
  return newArr;
}

function solve(array) {
  let Cend = -1;
  let Jend = -1;
  let work = [];
  work.length = array.length;

  let arr = sortWithIndex(array);
  for (let ind = 0; ind < arr.length; ind++) {
    let start = parseInt(arr[ind][0]);
    let end = parseInt(arr[ind][1]);
    let index = parseInt(arr[ind][2]);
    if (start < Cend && start < parseInt(Jend)) {
      return "IMPOSSIBLE";
    }
    if (start >= parseInt(Cend)) {
      Cend = end;
      work[index] = "C";
    } else if (start >= parseInt(Jend)) {
      Jend = end;
      work[index] = "J";
    }
  }
  return work.join("");
}

// Test cases matched. But WA on submission
