function solution(str1, str2) {
  var answer = 0;
  
  const set1 = makeSet(str1.toLowerCase())
  const set2 = makeSet(str2.toLowerCase())
  
  const set = new Set([...set1, ...set2]);
  let union = 0
  let intersection = 0
  
  // 교집합과 합집합 모두 개수만 세어주면 된다.
  // set으로 모든 원소를 나타냈을 때
  set.forEach(char => {
      const num1 = set1.filter(word => word === char).length
      const num2 = set2.filter(word => word === char).length
      union += Math.max(num1, num2)
      intersection += Math.min(num1, num2)
  })
  
  answer = union ? intersection / union : 1
  
  return parseInt(answer * 65536);
}

function makeSet(str) {
  const set = []
  for(let i = 0; i < str.length - 1; i++) {
      const word = str[i] + str[i+1]
      if(word.match(/[^a-zA-Z]/)) continue     
      set.push(word) 
  }
  
  return set
}