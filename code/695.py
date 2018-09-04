class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # Solution 1 120ms
        # def explore(y,x,explored,grid):
        #     num = 1
        #     leny = len(grid)
        #     lenx = len(grid[0])
        #     # print(lenx,leny)
        #     explored[y][x]=1
        #     if y-1 >=0:
        #         if grid[y-1][x] and not explored[y-1][x]:
        #             num += explore(y-1,x,explored,grid)
        #     if y+1 <leny:
        #         if grid[y+1][x] and not explored[y+1][x]:
        #             num += explore(y+1,x,explored,grid)
        #     if x-1 >=0:
        #         if grid[y][x-1] and not explored[y][x-1]:
        #             num += explore(y,x-1,explored,grid)
        #     if x+1 <lenx:
        #         if grid[y][x+1] and not explored[y][x+1]:
        #             num += explore(y,x+1,explored,grid)
        #     return num
        #
        # leny = len(grid)
        # lenx = len(grid[0])
        # max = 0
        # num = []
        # explored = [[0 for x in range(lenx)]for y in range(leny)]
        # for y in range(leny):
        #     for x in range(lenx):
        #         if not explored[y][x] and grid[y][x]:
        #             num = explore(y,x,explored,grid)
        #             if num > max: max = num
        # return max

        # Solution 2 56ms
        # m, n = len(grid), len(grid[0])
        #
        # def explore(y,x):
        #     num = 1
        #     grid[y][x] = 0
        #     if y-1 >= 0:
        #         if grid[y-1][x]:num += explore(y-1,x)
        #     if y+1 < m:
        #         if grid[y+1][x]:num += explore(y+1,x)
        #     if x-1 >= 0:
        #         if grid[y][x-1]:num += explore(y,x-1)
        #     if x+1 < n:
        #         if grid[y][x+1]:num += explore(y,x+1)
        #     return num
        #
        # max = 0
        # for y in range(m):
        #     for x in range(n):
        #         if grid[y][x]:
        #             num = explore(y,x)
        #             if num > max: max = num
        # return max


        # Solution 3 60ms
        leny,lenx = len(grid),len(grid[0])
        def explore(y,x):
            if 0<=y<leny and 0<=x<lenx and grid[y][x]:
                    grid[y][x] = 0
                    return 1+ explore(y-1,x)+explore(y+1,x)+explore(y,x-1)+explore(y,x+1)
            return 0

        area = [explore(y,x)for y in range(leny)for x in range(lenx)if grid[y][x]]
        return max(area) if area else 0

s = Solution()
grid = \
[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
print(s.maxAreaOfIsland(grid))