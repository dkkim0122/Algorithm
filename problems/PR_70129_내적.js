function solution(a, b) {
    
  const answer = a.reduce((acc, cur, i) => {
      return acc + a[i]*b[i]
  }, 0)  // 초기값 적어주지 않으면 초기값은 0번째 인덱스 값, 인덱스는 1부터 시작
  
  return answer;
}