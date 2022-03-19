function solution(n) {
  let answer = []
  const array = new Array(n).fill().map((_, i) => new Array(i+1))
  
  let x = -1
  let y = 0
  let count = 1
  let N = n
  while (N > 0){
      for (let i = 0; i < N; i++) array[++x][y] = count++
      for (let i = 0; i < N-1; i++) array[x][++y] = count++
      for (let i = 0; i < N-2; i++) array[--x][--y] = count++
      N -= 3        
  }
  
  for (let i = 0; i < n; i++){
      answer = answer.concat(array[i])
  }
  
  return answer
}