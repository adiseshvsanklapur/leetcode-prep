#logic: set up prefix and postfix integers
#make a res array of length nums to start
#then, for each value for res, multiply by pre
#do the same when iterating for post
#Time complexity O(N) because O(N)+O(N) operations to make the res
#space complexity O(N) to hold res, but O(1) auxiliary space
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums)
        pre=1
        for i in range(len(nums)):
            res[i]=pre
            pre*=nums[i]
        post=1
        for i in range(len(nums)-1,-1,-1):
            res[i]*=post
            post*=nums[i]
        return res