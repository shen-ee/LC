class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # if digits == "":
        #     return []

        dic = {}
        dic["1"] = []
        dic["2"] = ["a","b","c"]
        dic["3"] = ["d","e","f"]
        dic["4"] = ["g","h","i"]
        dic["5"] = ["j","k","l"]
        dic["6"] = ["m","n","o"]
        dic["7"] = ["p","q","r","s"]
        dic["8"] = ["t","u","v"]
        dic["9"] = ["w","x","y","z"]

        def combine(a,b):
            # if a == [] or b == []: 
            #     return a or b
            # return [i+j for i in a for j in b]
            return a or b if a == [] or b == [] else [i+j for i in a for j in b]

        def binary(s):
            # length = len(s)
            # if length == 1:
            #     return dic[s]
            # i = length/2
            # return combine(binary(s[:i]),binary(s[i:]))
            return dic[s] if len(s) == 1 else combine(binary(s[:len(s)/2]),binary(s[len(s)/2:]))
    
        return [] if digits == "" else binary(digits)

s = Solution()
re = s.letterCombinations("123")
print(re)
