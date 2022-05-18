function solution(lottos, win_nums) {
  const score = [6, 6, 5, 4, 3, 2, 1]
  
  
  let min_count = 0
  let zero_count = 0
  
  for(const lotto of lottos) {
      if (lotto === 0) zero_count++
      else if (win_nums.includes(lotto)) min_count++
  }
  
  let max_count = min_count + zero_count
  
  return [score[max_count], score[min_count]];
}