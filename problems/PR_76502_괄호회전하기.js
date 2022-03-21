function solution(s) {

  let total_count = 0;
  let clock_count = 0;
  let array = [...s];

  const dict = { "}": "{", "]": "[", ")": "(" };

  while (clock_count !== array.length) {
    const stack = [];
    for (let i = 0; i < array.length; i++) {
      const char = array[i];
      if (dict[char] === undefined) stack.push(char);
      else {
        if (stack[stack.length - 1] !== dict[char]) {
          stack.push(char)
          break;
        }
        stack.pop();
      }
    }

    
    if (stack.length === 0) total_count++;

    array.push(array.shift());
    clock_count++;
  }

  return total_count;
}

