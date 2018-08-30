class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Solution1
        # nums.sort()
        # if(len(nums)==1):
        #     return nums[0]
        # i = 0
        # while i < len(nums)-1:
        #     if(nums[i]!=nums[i+1]):
        #         return nums[i]
        #     i += 2
        # return nums[-1]

        # Solution 2
        # nums_pure = set(nums)
        # return sum(nums_pure)*2 - sum(nums)

        # Solution 3
        result = 0
        for num in nums:
            result ^= num
        return result

s = Solution()

list1 = [2,2,1]
list2 = [4,1,2,1,2]

print(s.singleNumber(list1))
print(s.singleNumber(list2))