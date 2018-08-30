class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if(matrix ==[]):
            return []
        y_max = len(matrix)-1
        x_max = len(matrix[0])-1
        x = 0
        y = 0
        isup = True
        rlist = []
        rlist.append(matrix[0][0])

        while(x!=x_max or y!=y_max):
            if isup:
                if y ==0 :
                    if x == x_max:
                        y += 1
                        isup = False
                    else:
                        x += 1
                        isup = False
                else:
                    if x == x_max:
                        y += 1
                        isup = False
                    else:
                        x += 1
                        y -= 1
                        isup = True
            else:
                if y == y_max:
                    if x == 0:
                        x += 1
                        isup = True
                    else:
                        x += 1
                        isup = True
                else:
                    if x == 0:
                        y += 1
                        isup = True
                    else:
                        y += 1
                        x -= 1
                        isup = False
            rlist.append(matrix[y][x])

        return rlist
m = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
m2 = [
 [ 1, 2, 3 ]
]

m3 = [[1],[2],[3]]
m4 = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ],
 [10,11,12]
]

m5 = []

s= Solution()
print(s.findDiagonalOrder(m5))


