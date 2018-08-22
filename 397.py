class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        num = n
        step = 0
        while(num!=1):
            if num == 3:
                return step +2
            else:
                if num%2==1:
                    if(num%4==1):
                        num = num-1
                    else:
                        num = num+1
                    step += 1
                else:
                    num = num/2
                    step += 1
        return step

s = Solution()
print(s.integerReplacement(3))