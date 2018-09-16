class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        # Solution 1 24ms
        matrix[::] = zip(*matrix[::-1])

mat = [
    [1,2],
    [3,4]

]

print(mat)
print(*mat)
mat[::] = [i[::-1]for i in mat][::-1]
# mat[::] = zip(*[i[::-1]for i in mat])
print(mat)