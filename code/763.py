class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        # Solution 1 32ms
        last = [0]*26
        for i in range(len(S)):
            last[ord(S[i])-ord('a')] = i
        max = -1
        ans=[]
        first = -1
        for i,char in enumerate(S):
            last_tmp = last[ord(char) - ord('a')]
            if i == max or (max == -1 and last_tmp == i):
                max = -1
                ans.append(i-first)
                first = i
            else:
                if last_tmp > max: max = last_tmp
        return ans

s = Solution()
input = "ababcbacadefegdehijhklij"
input = "caedbdedda"
input = "eaaaabaaec"
input = ""
print(s.partitionLabels(input))