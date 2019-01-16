class Solution:
    counter = 0
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        # Solution 1
        Solution.counter = 0
        num = []
        def swap(num,i,j):
            tmp = num[i]
            num[i] = num[j]
            num[j] = tmp

        def helper(num,starter):
            if starter == 0:
                Solution.counter += 1
                # counter += 1
                # print("hhh")
                return
            for i in range(starter,0,-1):
                swap(num,starter,i)
                if num[starter] % starter == 0 or starter % num[starter] == 0 :
                    helper(num,starter-1)
                swap(num,i,starter)

        for i in range(N+1):
            num.append(i)
        helper(num,N)
        return Solution.counter

s = Solution()
ret = s.countArrangement(1)
print(ret)