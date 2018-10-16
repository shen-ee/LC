class Solution(object):
    def partitionLabels(self, Houses, Stores):
        """
        :type S: str
        :rtype: List[int]
        """
        # Solution 1 32ms
        ans = []
        Stores.sort()
        print(Stores)
        def Helper(value):
            low = 0
            mid = len(Stores)/2
            high = len(Stores)-1
            print(Stores[low],Stores[mid],Stores[high])
            while low < high-1:
                
                if Stores[mid] < value :
                    low = mid 
                    mid = (high + mid)/2
                elif Stores[mid] > value :
                    high = mid 
                    mid = (low + mid)/2
                else:
                    low = mid 
                    high = mid + 1
                print(low,mid,high)
                
            print("low is "+str(Stores[low])+", distance is "+str(value-Stores[low]))
            print("high is "+str(Stores[high])+", distance is "+str(Stores[high]-value))
            print(low,mid,high)
            if value-Stores[low]<=Stores[high]-value:
                return Stores[low]
            else:
                return Stores[high]
        for i in Houses:
            ans.append(Helper(i))
        print(ans)
        



        return 

houses =[2,6,12,18]
stores =[5,8,9,20]
s = Solution()
s.partitionLabels(houses,stores)