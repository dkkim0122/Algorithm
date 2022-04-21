function solution(N, road, K) {
  const adj = Array.from({length : N + 1}, () => [])
  road.forEach(([a, b, cost]) => {
      adj[a].push({to: b, cost:cost})
      adj[b].push({to: a, cost:cost})
  })
  
  const dist = new Array(N + 1).fill(Infinity)
  const queue = []
  dist[1] = 0
  queue.push([1, dist[1]])
  
  while(queue.length) {
      const [cur, cur_cost] = queue.shift()
      if (cur_cost > dist[cur]) continue
      
      adj[cur].forEach((next) => {
          if (dist[next.to] > cur_cost + next.cost) {
              dist[next.to] = cur_cost + next.cost
              queue.push([next.to, dist[next.to]])
          }
      })
  }
  return dist.filter(a => a <= K).length
  
}