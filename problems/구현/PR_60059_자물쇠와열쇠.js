function solution(key, lock) {
  const N = lock.length
  const M = key.length
  
  // key를 수용할 수 있는 새 자물쇠(한변 길이 : 2*M+N+1)
  // 이 때 lock의 시작점은 M-1, 끝 점은 N+M-2
  const new_lock = new Array(N+2*M-2).fill().map(() => new Array(N+2*M-2).fill(0))
  for(let i = M-1; i <N+M-1; i++) {
      for(let j = M-1; j <N+M-1; j++) {
          new_lock[i][j] = lock[i-M+1][j-M+1]
      }
  }
  
  for(let i = 0; i < 4; i++) {
      key = rotate(key)  // 한 번 rotate한 key를 다시 rotate해야 한다.
      if(check(key, new_lock, N, M)) {
          return true
      }
  }
  
  return false;
}

function rotate(arr) {
  const new_arr = arr.map(row => [...row])
  const N = new_arr.length
  for(let i = 0; i < N; i++) {
      for(let j = 0; j < N; j++) {
          new_arr[j][N-i-1] = arr[i][j]
      }
  }
  return new_arr
}

// rotate한 key가 lock에 맞는지 체크
function check(arr, lock, N, M) {
  // key의 시작점을 정한다.
  for(let i = 0; i < N+M-1; i++) {
      for(let j = 0; j < N+M-1; j++) {
          if (match(arr, lock, i, j, N, M)) return true // key와 lock을 매칭한 다음에 메인 lock의 모든 값이 1이어야 한다.
      }
  }
  return false
}

function match(arr, lock, i, j, N, M) {
  const new_lock = lock.map(row => [...row])
  
  // key와 lock을 합치는 중
  for(let k = 0; k < M; k++) {
      for(let l = 0; l < M; l++) {
          if(new_lock[i+k][j+l] && arr[k][l]) return false  // 돌기가 만나서는 안된다.
          if(new_lock[i+k][j+l] || arr[k][l]) new_lock[i+k][j+l] = 1
      }
  }
  
  // lock을 확인하는 중
  for(let k = M-1; k < N+M-1; k++) {
      for(let l = M-1; l < N+M-1; l++) {
          if(new_lock[k][l] === 0) return false
      }
  }
  return true
}