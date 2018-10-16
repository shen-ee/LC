class Solution(object):
    def partitionLabels(self, Tree, D):
        """
        :type S: str
        :rtype: List[int]
        """
        # Solution 1 32ms
        length = len(Tree)
        ans = []
        history = [[-1 for i in range(D+1)] for j in range(length)]
        for i in range (length):
            curlevel = 0
            curnode = i
            while (curlevel != D):
                if curnode == -1:
                    curlevel = D
                    ans.append(-1)
                    break
                record = history[curnode][D-curlevel]
                if record != -1:
                    print("got")
                    ans.append(record)
                    curlevel = D
                else:
                    curlevel += 1
                    curnode = Tree[curnode] 
                    history[i][curlevel] = curnode
                    if curlevel == D:
                        ans.append(curnode)
                print(history,curlevel,curnode)
            print(ans)

        print(ans)
        return ans

tree = [-1,0,4,2,1]
d = 3
# tree = [-1,0,1,2,3]
# d = 2
s = Solution()
s.partitionLabels(tree,d)