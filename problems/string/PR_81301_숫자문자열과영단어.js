function solution(s) {
  var answer = 0;
  const numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
  
  const nums = s.split(/(\d)/).filter(el => el)
  const result = []
  for(let num of nums) {
      if(num.length === 1) {
          result.push(num)
          continue
      }
      let word = ''
      while(num.length) {
          word += num[0]
          num = num.slice(1)
          const idx = numbers.indexOf(word)
          if(idx !== -1) {
              result.push(idx)
              word = ''
          }
      }
  }
  
  return parseInt(result.join(""));
}