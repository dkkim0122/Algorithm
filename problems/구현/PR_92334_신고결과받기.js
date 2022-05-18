function solution(id_list, report, k) {
  const reports = [...new Set(report)].map(str => str.split(" "))
  const counts = new Map()
  
  reports.forEach(([user, bad]) => {
      counts.set(bad, counts.get(bad) + 1 || 1)
  })

  const users = new Map()
  reports.forEach(([user, bad]) => {
      if (counts.get(bad) >= k) {
          users.set(user, users.get(user) + 1 || 1)
      }
  })
  
  return id_list.map(id => users.get(id) || 0);
}