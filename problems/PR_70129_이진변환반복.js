function solution(s) {
  var answer = [];
  s = [...s]
  
  let change_count = 0
  let zero_count = 0

  while(s !== '1'){
      let new_array = []
      for (let i = 0; i < s.length; i++) {
          if (s[i] ==='0')
              zero_count += 1
          else
              new_array.push(s[i])
      }
      s = new_array.length.toString(2)
      change_count += 1
  }
  
  return [change_count, zero_count];
}