class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Solution 1 36ms
        # dic = {}
        # for i,num in enumerate(nums):
        #     if dic.has_key(target-num):
        #         return[dic[target-num],i]
        #     else:
        #         dic[num]=i

        # Solution 1+ 24ms
        dic = {}
        for i, num in enumerate(nums):
            aim = target - num
            if dic.has_key(aim):
                return [dic[aim], i]
            else:
                dic[num] = i


