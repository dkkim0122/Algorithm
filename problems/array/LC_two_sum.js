/**
 * O(n^2)로 해결
*/
var twoSum = function(nums, target) {
  for (let i = 0; i < nums.length - 1; i++) {
      for (let j = i + 1; j < nums.length; j++) {
          if (nums[i] + nums[j] === target) {
              return [i, j]
          }
      }
  }
};

/**
 * O(n)로 해결
 * for 문을 사용해서 돌리는 것이 아닌, Map을 사용하여 검색 시간 복잡도 O(n)로 만들 수 있다.
 * Map 자료구조를 사용할 수 있는 곳이 생각보다 많을 듯 하다.
*/
var twoSum = function(nums, target) {
    const map = new Map()
    
    for (let i = 0; i < nums.length; i++) {
        const diff = target - nums[i]
        if (map.has(diff)) {
            return [i, map.get(diff)]
        }
        map.set(nums[i], i)
    }
};