class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Exceed Time Limit
        # m = len(nums)
        # ans = [1 for i in range(m)]
        # print(m)
        # for i, num in enumerate(nums):
        #     print(i, num)
        #     for j in range(m):
        #         if j is not i:
        #             ans[j] =ans[j]*num
        #     print(ans)
        # return ans

        # Solution 1 116ms
        # m = len(nums)
        # res = [0 for i in range(m)]
        # tmp = 1
        # for i in range(0, m):
        #     res[i] = tmp
        #     tmp *= nums[i]
        # tmp = 1
        # for i in range(m-1, -1, -1):
        #     res[i] *= tmp
        #     tmp *= nums[i]
        # return res

        # Solution 2 96ms
        m = len(nums)
        res = []
        tmp = 1
        for num in nums:
            res.append(tmp)
            tmp *= num
        tmp = 1
        for i in range(m-1, -1, -1):
            res[i] *= tmp
            tmp *= nums[i]
        return res

s = Solution()
input = [1, 2, 3, 4]
print(s.productExceptSelf(input))