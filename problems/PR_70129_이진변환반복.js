function solution(s) {
  let answer = [0, 0]
  
  for(;;) {
      let after = s.split("0").join("")
      answer[1] += s.length - after.length
      answer[0] += 1
      s = after.length.toString(2)
  
      if(s === '1')
          break
  }
  return answer

}