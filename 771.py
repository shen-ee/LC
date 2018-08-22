class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        sum = 0
        for c in S:
            if c in J:
                sum+=1
        return sum

s = Solution()
print(s.numJewelsInStones("aA","aAAbbbb"))

print([i in "aA" for i in "aAAbbb"])

print([i in "a" for i in "aAAbbb"])

J = "aA"
S = "AAaajjj"

s = map(J.count,S)
print(s)
print(list(s))

J.count()

