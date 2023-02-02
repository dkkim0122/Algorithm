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

/**
 * O(m+n), Runtime 71 ms, Memory 43.7 MB
 * map은 하나만 만들고, 나머지 array를 순회하면서 result에 들어갈 숫자들을 찾는다.
 * 소요 시간은 이 방법이 더 큰데, map을 순회하는 것이 array를 순회하는 것보다 더 빨라서 그런지는 좀 더 봐야할 것 같다.
 */

var intersect = function(nums1, nums2) {
  const map = new Map()
  const result = []

  nums1.forEach(num => {
      map.get(num) ? map.set(num, map.get(num) + 1) : map.set(num, 1)
  })
  
  nums2.forEach((num) => {
      if (map.get(num)) {
        result.push(num)
        map.set(num, map.get(num) - 1)
      }
  })

  return result
};

/**
 * O(n), Runtime 58 ms, Memory 43 MB
 * 훨씬 이해하기 쉽고 성능도 나쁘지 않다.
 */

var intersect = function(nums1, nums2) {
  const result = []
  nums1 = nums1.sort((a, b) => a - b)
  nums2 = nums2.sort((a, b) => a - b)

  while (nums1.length > 0 && nums2.length > 0) {
      if (nums1[0] === nums2[0]) {
          result.push(nums1.shift())
          nums2.shift()
      }
      
      if (nums1[0] > nums2[0]) {
          nums2.shift()
      }

      if (nums1[0] < nums2[0]) {
          nums1.shift()
      }
  }

  return result
};