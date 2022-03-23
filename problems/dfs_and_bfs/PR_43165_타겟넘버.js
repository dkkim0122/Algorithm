function solution(numbers, target) {
    
  const need_visited = [[numbers[0], 1], [-numbers[0], 1]]
  const visited = new Array(numbers.length).fill(false)
  let total_count = 0
  
  while(need_visited.length) {
      const [number, count] = need_visited.shift()
      if (count === numbers.length) {
          if (number === target)
              total_count += 1
          continue
      }
      
      if (count < numbers.length){
          need_visited.push([number + numbers[count], count + 1])
          need_visited.push([number - numbers[count], count + 1])    
      }
      
  }
  
  return total_count;
}