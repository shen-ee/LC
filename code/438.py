class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        # Solution 1  Time Limit Exceeded
        # ans = []
        # # p = "".join((lambda x: (x.sort(), x)[1])(list(p)))
        # if s is None or len(s)<len(p):
        #     return []
        # for i in range(0,len(s)-len(p)+1):
        #     # print(i)
        #     pattern = p
        #     for j in range(i, i+len(p)):
        #         if s[j] in pattern:
        #             pattern = pattern.replace(s[j],"",1)
        #     if pattern == "":
        #         ans.append(i)
        if s is None or len(s)<len(p):
            return []
        ans = []
        right, left = 0, 0
        tobecontained = len(p)
        dic = [0]*26
        for c in p:
            dic[ord(c)-ord('a')] += 1
        while right < len(s):
            index_r = ord(s[right])-ord('a')
            if dic[index_r] > 0:
                tobecontained -=1
            dic[index_r] -= 1
            # print(right, tobecontained)
            right += 1
            while tobecontained == 0:
                # print(right,left)
                index_l = ord(s[left])-ord('a')
                if dic[index_l] == 0:
                    if right - left == len(p):
                        ans.append(left)
                    tobecontained += 1
                left += 1
                dic[index_l] += 1
        # print(p)
        return ans

so = Solution()
s = "cbaebabacd"
p = "abc"
print(so.findAnagrams(s,p))
