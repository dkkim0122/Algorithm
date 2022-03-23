function solution(begin, target, words) {
  if (words.indexOf(target) === -1) return 0
  const arr = new Array()
  
  const need_visit = [[begin, 0]]
  while (need_visit) {
    const [word, count] = need_visit.pop()

    if(word === target) {
      return count
    }

    words.forEach(next => {
      if (check(word, next))
        need_visit.push([next, count++])
    })
  }
  
  var answer = 0;
  return answer;
}

function check(str1, str2) {
  const a = str1.split("")
  const b = str2.split("")
  let count = 0
  a.forEach((char, i) => {
      if(char !== b[i])
          count++
  })
  if (count===1)
      return true
  else
      return false
}

console.log(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
console.log(check("hit", "hop"))