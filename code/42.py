class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height: return 0
        m = len(height)
        left, right= 0,m-1
        leftmax, rightmax = 0, 0
        res = 0
        while left != right:
            if height[left]<=height[right]:
                if height[left] > leftmax : leftmax = height[left]
                else: res += leftmax - height[left]
                left += 1
            else:
                if height[right] > rightmax: rightmax = height[right]
                else: res += rightmax - height[right]
                right -= 1
        return res
s = Solution()
input = [0,1,0,2,1,0,1,3,2,1,2,1]
print(s.trap(input))