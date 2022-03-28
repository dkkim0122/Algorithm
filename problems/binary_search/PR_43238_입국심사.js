function solution(n, times) {  
  let start = 0
  let end = times[times.length - 1] * n
  let mid = 0
  let answer = end
  while(start <= end) {
      mid = Math.floor((start + end) / 2)
      let available = times.reduce((acc, cur) => acc + Math.floor(mid / cur), 0)
      
      if (available >= n) {
          answer = Math.min(answer, mid)
          end = mid - 1
      } else {
          start = mid + 1
      }
      
  }
  
  return answer;
}