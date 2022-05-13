function solution(n, stations, w) {
  let answer = 0
  const area = 2 * w + 1
  
  let start = 1
  while(stations.length) {
      const end = stations[0] - w - 1
      const len = end - start
      answer += Math.floor(len / area) + 1

      start = stations[0] + w + 1
      stations.shift()
  }
  
  if (start <= n) {
      const len = n - start
      answer += Math.floor(len / area) + 1
  }
  
  return answer;
}