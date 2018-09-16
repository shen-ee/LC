class Solution(object):
    def totalNQueens(self, n):
        self.res = 0
        self.dfs([-1] * n, 0)
        return self.res

    def dfs(self, nums, index):
        if index == len(nums):
            self.res += 1
            return  # backtracking
        if index == len(nums):
            return
        for i in range(len(nums)):
            nums[index] = i
            if self.valid(nums, index):  # pruning
                self.dfs(nums, index + 1)

    def valid(self, nums, n):
        for i in range(n):
            if abs(nums[i] - nums[n]) == n - i or nums[i] == nums[n]:
                return False
        return True

s = Solution()
res = s.totalNQueens(4)
print(res)