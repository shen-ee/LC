class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # collect apperance index list of each number
        book = {}
        for index,num in enumerate(nums):
            if num not in book:
                book[num] = [index]
            else:
                book[num].append(index)

        
        # compute the degree of nums[]
        degree = 0
        maxlist = []  # record apperance index list  of number which appears 'degree' times， possibly more than one number
        for i in book:
            freq = len(book[i])
            if freq > degree:
                degree = freq
                maxlist = [book[i]]  # since a bigger degree is found, clear old records
            elif freq == degree:
                maxlist.append(book[i]) 

        # special case
        if degree == 1:
            return 1

        # find the shortest subarray
        minlength = float('inf')
        for i in maxlist:
            length = i[-1] - i[0] + 1
            minlength = min(length,minlength)
        return minlength
        
S = Solution()
S.findShortestSubArray([1,2,2,1,2,1,1,1,1,2,2,2])

