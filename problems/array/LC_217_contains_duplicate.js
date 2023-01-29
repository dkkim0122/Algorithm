/* https://leetcode.com/problems/contains-duplicate */
/**
  * 맨 처음 생각했던 방식은 브루트 포스와 같이 reduce 함수를 이용하여 모든 경우의 수를 찾아보는 것.
    * Runtime: 7728 ms / Memory: 52.5MB
    * 너무 느리다.
  * 두 번째
    * Set을 사용하여 배열의 중복을 제거한다. new Set().size와 원래 배열.length를 비교하여 중복되어 제거된 요소가 있는지를 확인.
    * Runtime: 98 ms / Memory: 55MB
 */

/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
  const setNums = new Set(nums)
  return nums.length !== setNums.size
};