function solution(begin, target, words) {
  if (!words.includes(target)) return 0
  const need_visit = [[begin, 0]]
  while (need_visit) {
    const [word, count] = need_visit.shift()

    if(word === target) {
      return count
    }

    words.forEach(next => {
      if (check(word, next))
        need_visit.push([next, count+1])
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

console.log(solution("hit", "cog", ["dog", "hot", "dot", "cog", "lot", "log"]))
console.log(check("hit", "hop"))