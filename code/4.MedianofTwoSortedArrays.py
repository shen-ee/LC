class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # Solution 1
        # num = nums1 + nums2
        # num.sort()
        # length = len(num)
        # if length %2 == 0:
        #     print(num[(length-2)/2]+num[length/2])/2
        # else:
        #     print(num[(length-1)/2])

        # Solution 2
        def helper(a,b,k):
            if a == []:
                return b[k]
            if b == []:
                return a[k]
            ia, ib = len(a) // 2 , len(b) // 2
            ma, mb = a[ia], b[ib]
            print(a,b,k)
            if ia + ib < k :
                if ma > mb:
                    return helper(a,b[ib+1:],k-ib-1)
                else:
                    return helper(a[ia+1:],b,k-ia-1)
            else:
                if ma > mb:
                    return helper(a[:ia],b,k)
                else:
                    return helper(a,b[:ib],k)

        l = len(nums1) + len(nums2)
        if l % 2 == 1:
            return helper(nums1, nums2, l // 2)
        else:
            print(l//2,helper(nums1, nums2, l // 2))
            print(l//2-1,helper(nums1, nums2, l // 2 - 1))
            return (helper(nums1, nums2, l // 2) + helper(nums1, nums2, l // 2 - 1)) / 2.   
        

s = Solution()
print(s.findMedianSortedArrays([1,3],[2,4]))
