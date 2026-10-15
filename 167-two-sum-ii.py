class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, (len(numbers)-1)
        while l<r:
            if numbers[r]+numbers[l]==target:
                return [l+1,r+1]
            elif numbers[l]+numbers[r]>target:
                r-=1
            elif numbers[l]+numbers[r]<target:
                l+=1

        return [l+1, r+1]

    #O(N) time complexity because have a loop iterating through the string
    #O(1) auxiliary space because all im recording is l and r temporary vars