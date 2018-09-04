class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # Solution 1 72ms
        if not grid:return 0
        m,n = len(grid),len(grid[0])
        def explore(y,x):
            if 0<=y<m and 0<=x<n and grid[y][x] == '1':
                    grid[y][x] = '0'
                    # map(explore, [y - 1, y + 1, y, y],[x, x, x - 1, x + 1])
                    explore(y - 1, x)
                    explore(y + 1, x)
                    explore(y, x - 1)
                    explore(y, x + 1)
            return 0

        islands = [explore(y,x)for y in range(m)for x in range(n)if grid[y][x] == '1']
        return len(islands) if islands else 0