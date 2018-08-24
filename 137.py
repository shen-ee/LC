class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Solution1 28ms
        # nums.sort()
        # if(len(nums)==1):
        #     return nums[0]
        # i = 0
        # while i < len(nums)-1:
        #     if(nums[i]!=nums[i+1] or nums[i]!=nums[i+2] or nums[i+1]!=nums[i+2]):
        #         return nums [i]^nums[i+1]^nums[i+2]
        #     i += 3
        # return nums[-1]

        # Solution 2 32ms
        # nums_pure = set(nums)
        # return (sum(nums_pure)*3 - sum(nums))/2

        # Solution 3 24ms
        x1 = 0
        x2 = 0
        for num in nums:
            x2 = x2 ^ (x1 & num)
            x1 = x1 ^ num
            mask = ~(x1&x2)
            x2 &= mask
            x1 &= mask

        return x1

s = Solution()

list1 = [2,2,3,2]
list2 = [0,1,0,1,0,1,99]

print(s.singleNumber(list1))
print(s.singleNumber(list2))