function solution(play_time, adv_time, logs) {
  play_time = toTime(play_time)
  adv_time = toTime(adv_time)
  
  // 각 초당 누적 시청자 수를 구할 것 -> 이때까지 보고 있는 시청자 수가 최대일 시점이 정답이다.
  const times = new Array(play_time).fill(0)
  
  logs.forEach((log) => { // 각 초마다 시청을 시작하는 시청자들의 수
      const nums = log.split("-")
      const start = toTime(nums[0])
      const end = toTime(nums[1])

      times[start]++
      times[end]--        
  })
  
  // 해당 초에서 시청하고 있는 시청자들의 수 : 누적합
  for(let i = 1; i <= play_time; i++) {
      times[i] += times[i-1]
  }
  
  // 각 초마다 시청하고 있는 시청자들의 누적된 시청 시간 : 누적합의 누적합
  for(let i = 1; i <= play_time; i++) {
      times[i] += times[i-1]
  }

  let max = times[adv_time-1]
  let idx = 0
  
  // 가장 많은 사람들이 시청하는 구간의 누적된 시청 시간
  // 해당 구간 누적 시청 시간 = end시청시간 - start시청시간
  for(let i = adv_time-1; i < play_time; i++){
      const view = times[i] - times[i-adv_time]
      if(max < view) {
          max = view
          idx = i-adv_time+1
      }
  }

  return toTimeString(idx);
}

function toTime(str) {
  const times = str.split(':')
  return times[0] * 3600 + times[1] * 60 + times[2]*1
}

function toTimeString(time) {
  let H = time / 3600 >> 0
  let M = (time / 60 >> 0) % 60
  let S = time % 60
  
  H = H >= 10 ? H : '0' + H
  M = M >= 10 ? M : '0' + M
  S = S >= 10 ? S : '0' + S
  
  return `${H}:${M}:${S}`
}