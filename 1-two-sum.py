class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        #logic
        #use a hashmap to store value and index of arr elements so far
        #before adding arr element to dict, check if difference in element
        #if so, just return
        #otherwise, continue adding
        #if difference never found, then false
        dct = {}
        for i in range(len(nums)):
            if target-nums[i] in dct:
                return [dct[target-nums[i]], i]
            else:
                dct[nums[i]] = i
        return False