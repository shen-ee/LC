class Solution(object):
    def maskPII(self, S):
        """
        :type S: str
        :rtype: str
        """
        rstr = ""

        if "@"in S:#邮箱
            #print("email")
            S = S.lower()
            name1 = S.split('@')[0]
            name2 = S.split('@')[1]
            S = name1[0]+"*****"+name1[-1]+"@"+name2
            rstr = S
        else:#电话
            #print("phone")
            for c in S:
                if c in "+-() ":
                    S = S.replace(c,'')
            last = S[-4:]
            if(len(S)>10):
                first = S[:len(S)-10]
                S = "+"+"*"*len(first)+"-***-***-"+last
            else:
                S = "***-***-"+last
            rstr = S
        #print(rstr)
        return rstr

s = Solution()
ex1 = "LeetCode@LeetCode.com"
ex2 = "AB@qq.com"
ex3 = "1(234)567-890"
ex4 = "86-(10)12345678"
s.maskPII(ex1)
s.maskPII(ex2)
s.maskPII(ex3)
s.maskPII(ex4)