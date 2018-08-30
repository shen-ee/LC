class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        list = [1]
        ans = 0
        for i,c in enumerate(s):# xrange(1,len(s))
            if(i==len(s)-1):
                break;
            if(s[i]==s[i+1]):
                list[-1]+=1
            else:
                list.append(1)

        for i,s in enumerate(list):
            if (i == len(list) - 1):
                break;
            ans += min(list[i],list[i+1])
        return ans
        
