class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        if not people:
            return []
        collection = []
        hyperlist=[[] for row in range(1101)]
        newlist = []

        people.sort(key=lambda person: person[0], reverse=True) # from high to low

        pointer = -1
        for person in people:
            height,num = person[0],person[1]
            if height not in collection :
                collection.append(height)
                pointer+=1
            hyperlist[pointer].append(num)

        #print(hyperlist)
        #print(collection)

        pointer = 0
        for height in collection: # from high to low
            hyperlist[pointer].sort() # from small to large
            #print(hyperlist[height])
            for num in hyperlist[pointer]:
                person = [height,num]
                #print(person)
                newlist.insert(num,person)
            pointer += 1

        return newlist

s = Solution()

input = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

print(s.reconstructQueue(input))

input.sort(key=lambda person : person[0] , reverse=True)
print(input)