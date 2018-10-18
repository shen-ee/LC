import Queue
import math
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution(object):
#     def mergeKLists(self, lists):
#         """
#         :type lists: List[ListNode]
#         :rtype: ListNode
#         """
#         q = Queue.PriorityQueue()
#         root = ListNode(None)
#         curnode = root
#         for node in lists:
#             curnode = q.get()
#             while curnode:
#                 root.put(curnode.val,curnode.value)
#                 curnode = curnode.next if curnode.next

def cosine(x,y,diction):
    length = len(diction.items()[0][1])
    a, b, c = 0, 0, 0
    for i in range(length):
        a += pow(diction[x][i],2)
        b += pow(diction[y][i],2)
        c += diction[x][i]*diction[y][i]
    res = c/(math.sqrt(a)*math.sqrt(b))
    print("cosine similarity between "+x+" and "+y+": "+str(res))
    return 

dic={}
dic["wine"] = [4,2,0,2]
dic["keyboard"] = [1,10,4,1]
dic["beer"] = [8,3,1,1]
dic["memory"] = [0,6,3,0]

print(dic.items()[0])

total = 4+1+8+2+10+3+6+4+1+3+2+1+1
re = (2.0/total)/((8.0/total)*(4.0/total))
print(math.log(re,2))
a = 8*8 + 3*3 +1 +1
b = 6*6 + 9
c = 21
print(c/(math.sqrt(a)*math.sqrt(b)))
cosine("wine","beer",dic)
cosine("keyboard","memory",dic)
print ("")
cosine("wine","keyboard",dic)
cosine("beer","memory",dic)
print ("")
cosine("wine","memory",dic)
cosine("beer","keyboard",dic)
print ("")
cosine("beer","keyboard",dic)
cosine("wine","keyboard",dic)

            