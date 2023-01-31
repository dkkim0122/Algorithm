/** https://leetcode.com/problems/merge-sorted-array */

/**
  앞이 아닌 뒤에서부터 시작한다. 
  m의 경우 시작값이 0이라 해도 결국 num1의 결과가 중요하므로 while 조건문에서 없어도 되지만,
  n의 경우 자신의 값을 num1에 주어야 하기 때문에 while 조건문에 포함하여야 한다.
  array[-1]의 값은 undefined이나, 이에 해당하는 경우의 수는 else로 몰아버렸으므로 edge case에서도 해당 코드가 동작한다.
  */
  var merge = function(nums1, m, nums2, n) {
    let insertIndex = m + n - 1
    m -= 1
    n -= 1

    while (n >= 0) {
        if (nums1[m] >= nums2[n]) {
            nums1[insertIndex] = nums1[m]
            m -= 1
        } else {
            nums1[insertIndex] = nums2[n]
            n -= 1
        }

        insertIndex -= 1
    }      
};