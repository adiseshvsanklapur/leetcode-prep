#problem description: the problem is to group
#anagrams together in a list of strings.

from ast import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            count = [0]*26 #a to z counts
            for i in s:
                count[ord(i)-ord("a")] += 1
            res[tuple(count)].append(s)

        return list(res.values())

#time complexity: O(m*n) where m is the average length of
# each string and n is the number of strings
#space complexity: O(n) where n is the number of strings