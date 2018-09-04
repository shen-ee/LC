class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # Solution 1 60ms
        # sum = 0
        # for i in range(len(nums)):
        #     num = nums.pop(0)
        #     if num is not 0:
        #         nums.append(num)
        #     else:
        #         sum += 1
        # [nums.append(0) for i in range(sum)]
        # return nums

        # Solution 2 264ms
        # for num in nums:
        #     if num is 0:
        #         nums.remove(num)
        #         nums.append(0)
        # return nums

        # Solution 3 40ms
        count = nums.count(0)
        nums = [i for i in nums if i != 0] + [0] * count

        # Wrong Solution
        # k = 0
        # for i in nums:
        #     if i is 0:
        #         nums.remove(i)
        #         k += 1
        # nums.extend([0] * k)
        # return nums


s = Solution()
Input = [0,4,0,0,0,0,1]
Input = [0,1,0,3,12]
Input = [0,0,1]
print(s.moveZeroes(Input))