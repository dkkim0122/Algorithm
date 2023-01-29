/* https://leetcode.com/problems/contains-duplicate */
/**
 * 맨 처음 생각했던 방식은 브루트 포스와 같이 reduce 함수를 이용하여 모든 경우의 수를 찾아보는 것.
    * Runtime: 7728 ms / Memory: 52.5MB
    * 너무 느리다.
 */

/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
  const numArray = []

  for (const num of nums) {
      if (numArray.includes(num)) {
          return true
      }
      numArray.push(num)
  }
  
  return false
};