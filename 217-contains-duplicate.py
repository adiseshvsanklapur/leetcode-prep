#check if a list contains duplicate elements

#logic
#can use a set to check for duplicates

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        if len(set(nums))==len(nums):
            return False
        else:
            return True

#O(n) time complexity --> n being set size
#O(n) space complexity --> n being set size