function solution(arr) {
  let total_zero = 0
  let total_one = 0
  let n = arr[0].length
  
  function get_count(n, x0, x1, y0, y1) {
      if (n === 1) {
          if (arr[x0][y0] === 0)
              total_zero++
          else 
              total_one++
          return 
      }
          
      let zero = 0
      let one = 0
      for(let x = x0; x < x1; x++){
          for (let y = y0; y < y1; y++){
              if (arr[x][y] === 0) zero++
              else one++
          }
      }
      if (zero === n**2)
          total_zero++
      else if(one === n**2)
          total_one++
      else{
          get_count(n/2, x0, x0 + n/2, y0, y0 + n/2)
          get_count(n/2, x0, x0 + n/2, y0 + n/2, y1)
          get_count(n/2, x0 + n/2, x1, y0, y0 + n/2)
          get_count(n/2, x0 + n/2, x1, y0 + n/2, y1)
      }
  }
  
  let N = arr[0].length
  get_count(N, 0, N, 0, N)
  
  return [total_zero, total_one];
}