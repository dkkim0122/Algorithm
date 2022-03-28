function solution(n, left, right) {
  var answer = [];
  
  
  for(let i = left; i <= right; i++){
      const N = Math.floor(i / n) + 1
      const value = i % n < N ? N : i % n + 1
      answer.push(value)
  }
  
  return answer;
}