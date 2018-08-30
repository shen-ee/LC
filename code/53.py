class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cursum = maxsum = nums[0]
        if(len(nums)==1):
            return maxsum
        for c in nums[1:]:
            cursum = max(c,c+cursum)
            maxsum = max(cursum,maxsum)
        return maxsum

s = Solution()
nums = [-1,2]
print(s.maxSubArray(nums))