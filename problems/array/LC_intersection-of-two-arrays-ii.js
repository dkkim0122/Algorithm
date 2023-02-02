/** https://leetcode.com/problems/intersection-of-two-arrays-ii */

/**
 * O(m+n), Runtime 54 ms, Memory 43.9 MB
 * Map 자료구조를 이용하여 각 array에 숫자가 각각 몇 개씩 들었는지를 확인한다.
 * Map은 forEach를 이용하여 순회할 수 있다.
 */

var intersect = function(nums1, nums2) {
  const map1 = new Map()
  const map2 = new Map()
  const result = []

  function makeMap(map, array) {
      array.forEach(num => {
          map.get(num) ? map.set(num, map.get(num) + 1) : map.set(num, 1)
      })
  }
  
  makeMap(map1, nums1)
  makeMap(map2, nums2)

  map1.forEach((count1, num) => {
      const count2 = map2.get(num)
      if (count2) {
          const count = Math.min(count1, count2)
          for(let i = 0; i < count; i++) {
              result.push(num)
          }
      }
  })

  return result
};