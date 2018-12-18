import Queue
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # # Solution 1
        # q = Queue.PriorityQueue()
        # root = ListNode(None)
        # curnode = root
        # for node in lists:
        #     if node is None :
        #         continue
        #     q.put((node.val,node))
        # while q.qsize() > 0:
        #     curnode.next = q.get()[1]
        #     curnode = curnode.next
        #     if curnode.next:
        #         q.put((curnode.next.val, curnode.next))
        # return root.next

        # Solution 2
        ans = []
        for list in lists:
            while list:
                ans.append(list.val)
                list = list.next
        head = root = ListNode(None)
        for i in sorted(ans):
            head.next = ListNode(i)
            head = head.next
        return root.next




            