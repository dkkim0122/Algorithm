function solution(numbers, target) {
  const need_visited = [[0, 0]];
  let total_count = 0;
  
  function dfs(number, count) {
      if (count < numbers.length) {
        dfs(number + numbers[count], count + 1);
        dfs(number - numbers[count], count + 1);
      } else {
        if (number === target) total_count += 1;
      }
  }
  
  dfs(0,0)

  return total_count;
}