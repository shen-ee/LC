class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        # Solution 1
        time = [int(i) for i in time.replace(":","")]
        digits = sorted(time)

        def Helper():
            for i in range(3,-1,-1):
                for j in sorted(digits):
                    # if i == 3:
                    #     if j > time[i]:
                    #         time[i] = j
                    #         return 
                    # elif i == 2:
                    #     if j > time[i] and j < 6:
                    #         time[i] = j
                    #         return 
                    # elif i == 1:
                    #     if j > time[i] and (time[0] < 2 or j < 4):
                    #         time[i] = j
                    #         return
                    # else:
                    #     if j > time[i] and j < 3:
                    #         time[i] = j
                    #         return 
                    if j > time[i] and (i == 3 or (i == 2 and j < 6) or (i == 1 and (time[0] < 2 or j < 4)) or (i == 0 and j < 3)) :
                        time[i] = j 
                        return time
                time[i] = digits[0]

        Helper()
        time.insert(2,":")
        return str("".join ([str(i) for i in time]))

s = Solution()
re = s.nextClosestTime("17:28")
print(re)