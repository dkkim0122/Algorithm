function solution(array, commands) {
  let answer = []
  commands.map((command) => {
      let [start, end, index] = command
      let new_array = array.slice(start - 1, end).sort((a,b) => {return a-b})
    answer.push(new_array[index - 1])
  })
  return answer;
}