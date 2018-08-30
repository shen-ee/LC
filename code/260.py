class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Solution1 28ms
        # nums.sort()
        # list = []
        # i = 0
        # while i < len(nums)-1:
        #      if(nums[i]!=nums[i+1]):
        #          list.append(nums[i])
        #          i += 1
        #      else:
        #          i += 2
        # if(i == len(nums)-1):
        #     list.append(nums[-1])
        # return list

        # Solution 2 24ms
        numset = set()
        for num in nums:
            if num not in numset:
                numset.add(num)
            else:
                numset.remove(num)
        return list(numset)

s = Solution()

list1 = [1,2,1,3,2,5]

print(s.singleNumber(list1))