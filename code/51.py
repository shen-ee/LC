class Solution(object):
    def solveNQueens(self, n):
        res = []
        self.dfs([-1] * n, 0, [], res)
        return res

    def dfs(self, nums, index, path, res):
        if index == len(nums):
            res.append(path)
            return  # backtracking
        if index == len(nums):
            return
        for i in range(len(nums)):
            nums[index] = i
            if self.valid(nums, index):  # pruning
                n = i
                self.dfs(nums, index + 1, path + ["."*i+"Q"+"."*(len(nums)-i-1)], res)

    def valid(self, nums, n):
        for i in range(n):
            if abs(nums[i] - nums[n]) == n - i or nums[i] == nums[n]:
                return False
        return True

s = Solution()
res = s.solveNQueens(4)
print(res)