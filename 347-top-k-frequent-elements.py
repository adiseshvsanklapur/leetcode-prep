#logic is to use a dictionary to count the freq of each element
# and then make a list where the index is the count and the value is the list of
# elements that have that frequency

from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        ct = defaultdict(int)
        freq = [[] for i in range(len(nums)+1)]

        for n in nums:
            ct[n] += 1
        for i, c in ct.items():
            freq[c].append(i)

        res = []
        for i in range(len(freq)-1, 0, -1):
            for j in freq[i]:
                res.append(j)
                if len(res)==k:
                    return res


#Time Complexity: O(N) because we iterate through the list of numbers once to coun
# frequencies and once more to build the frequency list,
# and then we iterate through the frequency list to get the top k elements.

#Space Complexity: O(N) because we use a dictionary to count frequencies
# and a list to store the frequency buckets