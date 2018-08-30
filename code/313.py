class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        totalPrime = len(primes)
        uglies = [0]*n
        uglies[0] = 1
        pointer = [0]*totalPrime
        for i in range(1,n):
            last = uglies[i-1]
            answer = last * primes[-1]
            answerPrime = []
            for index,prime in enumerate(primes):
                candidate = uglies[pointer[index]]*prime
                if(candidate > last and candidate<answer):
                    answerPrime = []
                    answer = candidate
                    answerPrime.append(index)
                elif(candidate > last and candidate == answer):
                    answerPrime.append(index)
            #print(answerPrime)
            uglies[i] = answer
            #print(answerPrime)
            for p in answerPrime:
                pointer[p] += 1
            #print(uglies)
        return uglies[-1]

s = Solution()
input = 2
primes = [2]
#input = 10000
#primes = [7,19,29,37,41,47,53,59,61,79,83,89,101,103,109,127,131,137,139,157,167,179,181,199,211,229,233,239,241,251]
input = 15
primes = [3,5,7,11,19,23,29,41,43,47]
print(s.nthSuperUglyNumber(input,primes))