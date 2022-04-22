function solution(n, words) {
  let word_map = new Map()
  word_map.set(words[0], true)
  
  for (let i = 1; i < words.length; i++) {
      if (words[i][0] !== words[i-1][words[i-1].length - 1] || word_map.get(words[i])) {
          const num = i % n + 1
          const sequence = parseInt(i / n) + 1
          return [num, sequence]            
      }

      word_map.set(words[i], true)
  }
  
  return [0,0];
}