# https://leetcode.com/problems/group-anagrams

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = defaultdict(list)
        
        while strs:
            string = strs.pop()
            temp = ''.join(sorted(string))
            dict[temp].append(string)
    
        return list(dict.values())