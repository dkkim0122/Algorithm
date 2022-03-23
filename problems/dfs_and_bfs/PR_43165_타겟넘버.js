function solution(numbers, target) {
  const need_visited = [[0, 0]];
  let total_count = 0;
  

  while (need_visited.length) {
      const [number, count] = need_visited.pop();

      if (count < numbers.length) {
        need_visited.push([number + numbers[count], count + 1]);
        need_visited.push([number - numbers[count], count + 1]);
      } else {
        if (number === target) total_count += 1;
      }
}

return total_count;
}