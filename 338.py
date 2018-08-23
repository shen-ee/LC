class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """

        # Solution 1
        # list = []
        # for c in range(0,num+1):
        #    list.append(str(bin(c)).count('1'))

        # Solution2
        # list = [0]*(num+1)
        # for index in range(0,num+1):
        #    list[index] = list[index>>1] + (index&1)

        # Solution3
        list = [0]
        while len(list) <= num:
            list += [i + 1 for i in list]
        list = list[:num+1]
        return list

s = Solution()

num = 5

print(s.countBits(num))