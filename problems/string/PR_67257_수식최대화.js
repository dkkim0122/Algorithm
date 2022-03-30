function solution(expression) {
  let answer = []
  const opers = [
      ['*', '+', '-'],
      ['*', '-', '+'],
      ['+', '*', '-'],
      ['+', '-', '*'],
      ['-', '*', '+'],
      ['-', '+', '*']
  ]
  
  for(let ops of opers) {
      let temp = expression.split(/([^0-9])/)
      for (let op of ops) {
          while(temp.includes(op)) {
              const idx = temp.indexOf(op)
              temp.splice(idx - 1, 3, eval(temp.slice(idx - 1, idx + 2).join("")))
          }    
      }
      answer.push(Math.abs(temp))
  }
  return Math.max(...answer)
}