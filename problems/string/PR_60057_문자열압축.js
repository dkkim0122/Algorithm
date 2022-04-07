function solution(s) {
  var answer = s.length;
  
  for (let i = 1; i <= parseInt(s.length / 2); i++) {
      let result = ''
      let word = s.slice(0, i)
      let string = s.slice(i)
      let count = 1
      
      while(string.length) {
          if (word === string.slice(0, i)) {
              count++
          }
          else {
              if (count >= 2) {
                  result += count + word
                  count = 1
              }
              else result += word
              
              word = string.slice(0, i)
          }
          string = string.slice(i)
      }
      if (count >= 2) result += count + word
      else result += word
      
      if (result.length < answer) answer = result.length
  }
  
  
  return answer;
}