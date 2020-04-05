// const input = [
//   "3",
//   "4",
//   "1 2 3 4",
//   "2 1 4 3",
//   "3 4 1 2",
//   "4 3 2 1",
//   "4",
//   "2 2 2 2",
//   "2 3 2 3",
//   "2 2 2 3",
//   "2 2 2 2",
//   "3",
//   "2 1 3",
//   "1 3 2",
//   "1 2 3",
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
  console.log(`Case #${i}: ${solve(arr, N)}`);
}

function solve(mat, N = 4) {
  let trace = 0;
  let latinRow = 0;
  let latinCol = 0;
  for (let i = 0; i < N; i++) {
    trace += parseInt(mat[i][i]);
    let objRow = {};
    for (let j = 0; j < N; j++) {
      if (objRow[mat[i][j]]) {
        latinRow++;
        break;
      } else {
        objRow[mat[i][j]] = true;
      }
    }
    let objCol = {};
    for (let k = 0; k < N; k++) {
      if (objCol[mat[k][i]]) {
        latinCol++;
        break;
      } else {
        objCol[mat[k][i]] = true;
      }
    }
  }
  return [trace, latinRow, latinCol].join(" ");
}

console.log(solve(mat, 4));
