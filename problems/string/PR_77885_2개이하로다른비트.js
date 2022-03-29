function solution(numbers) {
  let answer = [];
  numbers.forEach((num) => answer.push(check(num)));
  console.log(check(7));
  return answer;
}

function check(num) {
  let binary = num.toString(2).split("");
  binary.reverse().push("0");
  for (let i = 0; i < binary.length; i++) {
    if (binary[i] === "0") return num + 2 ** i;
    else if (binary[i] === "1" && binary[i + 1] === "0") return num + 2 ** i;
  }
}
