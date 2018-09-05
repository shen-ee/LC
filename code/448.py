class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Solution 1 252ms
        # for num in nums:
        #     index = abs(num)-1
        #     nums[index]= -abs(nums[index])
        # return [i+1for i in range(0,len(nums)) if nums[i]>0]

        # Solution 2 136ms
        ans = [0]*(len(nums)+1)
        for num in nums:
            ans[nums]= -1
        return [i for i in range(1,len(nums)+1) if not ans[i]]


s = Solution()
input = [4,3,2,7,8,2,3,1]
print(s.findDisappearedNumbers(input))