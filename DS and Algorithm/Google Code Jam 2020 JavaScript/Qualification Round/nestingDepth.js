// const input = ["4", "0000", "101", "111000", "1"];
const fs = require("fs");
const input = fs.readFileSync(0, "utf8").trim().split("\n");
let T = input[0];
for (let i = 1; i <= T; i++) {
  console.log(`Case #${i}: ${solve(input[i])}`);
}

function solve(s) {
  let bracket = 0;
  let nestedBracket = "";
  let left = "";
  let right = "";
  if (s.length === 1) {
    nestedBracket += "(".repeat(s) + s + ")".repeat(s);
  } else {
    for (let index = 0; index < s.length; index++) {
      if (index === 0) {
        left = parseInt(s[index]);
        right = parseInt(s[index]) - parseInt(s[index + 1]);
      } else if (parseInt(index) === parseInt(s.length - 1)) {
        left = parseInt(s[index]) - parseInt(s[index - 1]);
        if (left > 0) {
          nestedBracket += "(".repeat(left);
          bracket += left;
        }
        right = bracket;
        nestedBracket += parseInt(s[index]);
        nestedBracket += ")".repeat(right);
        break;
      } else {
        left = parseInt(s[index]) - parseInt(s[index - 1]);
        right = parseInt(s[index]) - parseInt(s[index + 1]);
      }
      if (left > 0) {
        nestedBracket += "(".repeat(left);
        bracket += left;
      }
      nestedBracket += parseInt(s[index]);
      if (right >= 0) {
        nestedBracket += ")".repeat(right);
        bracket -= right;
      }
    }
  }
  return nestedBracket;
}
