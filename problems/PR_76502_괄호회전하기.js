function solution(s) {
  var answer = -1;

  let total_count = 0;
  let clock_count = 0;
  let array = [...s];

  while (clock_count !== array.length) {
    let high_stack = [];
    let mid_stack = [];
    let low_stack = [];
    for (let i = 0; i < array.length; i++) {
      if (array[i] === "]" && high_stack[high_stack.length - 1] === "[") {
        high_stack.pop();
      } else if (array[i] === "[" || array[i] === "]")
        high_stack.push(array[i]);

      else if (array[i] === "}" && mid_stack[mid_stack.length - 1] === "{") {
        mid_stack.pop();
        continue;
      } else if (array[i] === "{" || array[i] === "}")
      mid_stack.push(array[i]);

      else if (array[i] === ")" && low_stack[low_stack.length - 1] === "(") {
        low_stack.pop();
        continue;
      } else if (array[i] === "(" || array[i] === ")")
      low_stack.push(array[i]);
    }

    if (high_stack.length === 0 && mid_stack.length === 0 && low_stack.length === 0 ) {
      total_count++;
    }

    let s0 = array[0];
    array = array.slice(1)
    array.push(s0)

    clock_count++;
  }

  return total_count;
}

console.log(solution("[(]){}"));
