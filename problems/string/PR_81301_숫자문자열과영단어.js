function solution(s) {
  const words = {
      'zero': '0',
      'one': '1',
      'two': '2',
      'three': '3',
      'four': '4',
      'five': '5',
      'six': '6',
      'seven': '7',
      'eight': '8',
      'nine': '9',
  }
  
  for(const [key, value] of Object.entries(words)) {  // 일반 객체이므로 Object.entries 사용
      const pattern = RegExp(key, 'g')
      s = s.replace(pattern, value)
  }
  
  
  return parseInt(s)
}